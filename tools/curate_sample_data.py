from __future__ import annotations

import argparse
import io
import shutil
import zipfile
from pathlib import Path

import pandas as pd

SOURCE_REPOSITORY = "https://github.com/pdecampossouza/Pipeline-for-Oral-Health-Images"
SOURCE_VERSION = "e23dcdae657f4f999d2e126cee673ce0b4cc25b7"
ADULT_COLLECTION = "Pranchetas fotografias - dentição permanente - CPOD treinamento"
PEDIATRIC_COLLECTION = "Pranchetas fotografias - dentição decídua - Oclusão treinamento"


def _original_rows(manifest: pd.DataFrame, collection: str) -> pd.DataFrame:
    df = manifest.loc[manifest["pdf_base"].eq(collection)].copy()
    df = df.loc[~df["filepath"].str.startswith(("clusters/", "images_by_view/"))]
    return df


def select_sample_rows(manifest: pd.DataFrame, collection: str, group: str, volunteers: int = 10) -> pd.DataFrame:
    df = _original_rows(manifest, collection)
    eligible=[]
    for volunteer, g in df.groupby("voluntario"):
        if g["seq"].nunique() >= 2:
            eligible.append(volunteer)
    chosen=sorted(eligible)[:volunteers]
    if len(chosen) < volunteers:
        raise ValueError(f"Collection '{collection}' has only {len(chosen)} volunteers with at least two sequences; need {volunteers}.")
    rows=[]
    for volunteer in chosen:
        g=df.loc[df["voluntario"].eq(volunteer)].sort_values(["seq","filepath"])
        picks=pd.concat([g.iloc[[0]], g.iloc[[-1]]]).drop_duplicates("filepath")
        if len(picks) != 2:
            raise ValueError(f"Volunteer {volunteer} does not provide two distinct source images in '{collection}'.")
        rows.append(picks)
    out=pd.concat(rows, ignore_index=True)
    records=[]
    for idx,row in out.iterrows():
        suffix=Path(row["filepath"]).suffix.lower() or ".jpg"
        sample_id=f"{group}_{idx+1:03d}"
        records.append({
            "sample_id": sample_id,
            "group": group,
            "original_filename": Path(row["filepath"]).name,
            "original_collection": collection,
            "volunteer_id": int(row["voluntario"]),
            "sequence": int(row["seq"]),
            "source_repository": SOURCE_REPOSITORY,
            "source_path": row["filepath"],
            "source_version": SOURCE_VERSION,
            "starter_purpose": "demonstration_only",
            "sample_filename": f"{sample_id}{suffix}",
        })
    return pd.DataFrame(records)


def _read_manifest(z: zipfile.ZipFile) -> tuple[str, pd.DataFrame]:
    candidates=[n for n in z.namelist() if n.endswith("metadata/manifest.csv")]
    if len(candidates) != 1:
        raise FileNotFoundError("Could not uniquely locate metadata/manifest.csv in source ZIP")
    manifest_name=candidates[0]
    root=manifest_name[: -len("metadata/manifest.csv")]
    return root, pd.read_csv(io.BytesIO(z.read(manifest_name)))


def _materialize_group(z: zipfile.ZipFile, root: str, rows: pd.DataFrame, dest: Path) -> None:
    image_dir=dest/"images"
    image_dir.mkdir(parents=True, exist_ok=True)
    for row in rows.itertuples(index=False):
        member=root + row.source_path
        if member not in z.namelist():
            raise FileNotFoundError(f"Source ZIP member not found: {row.source_path}")
        target=image_dir/row.sample_filename
        with z.open(member) as src, target.open("wb") as dst:
            shutil.copyfileobj(src,dst)
    rows.to_csv(dest/"metadata.csv", index=False)


def materialize_samples(
    source_zip: str | Path,
    output_root: str | Path,
    adult_collection: str = ADULT_COLLECTION,
    pediatric_collection: str = PEDIATRIC_COLLECTION,
    volunteers: int = 10,
) -> dict[str, Path]:
    source_zip=Path(source_zip)
    output_root=Path(output_root)
    with zipfile.ZipFile(source_zip) as z:
        root,manifest=_read_manifest(z)
        adult=select_sample_rows(manifest,adult_collection,"adult",volunteers)
        pediatric=select_sample_rows(manifest,pediatric_collection,"pediatric",volunteers)
        adir=output_root/"data"/"sample_adult"
        pdir=output_root/"data"/"sample_pediatric"
        _materialize_group(z,root,adult,adir)
        _materialize_group(z,root,pediatric,pdir)
    return {"adult": adir, "pediatric": pdir}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-zip", required=True)
    parser.add_argument("--output-root", default=".")
    args=parser.parse_args()
    paths=materialize_samples(args.source_zip,args.output_root)
    print(f"Adult sample: {paths['adult']}")
    print(f"Pediatric sample: {paths['pediatric']}")


if __name__ == "__main__":
    main()
