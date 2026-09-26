from pathlib import Path
import io, zipfile
import pandas as pd
import pytest

from tools.curate_sample_data import select_sample_rows, materialize_samples


def synthetic_manifest():
    rows=[]
    for v in range(1,11):
        for seq in [1,2,3]:
            rows.append({'filepath':f'Collection/img_v{v}_{seq}.jpg','pdf_base':'Collection','voluntario':v,'seq':seq,'bytes':10})
    return pd.DataFrame(rows)


def test_selects_min_and_max_per_volunteer():
    out=select_sample_rows(synthetic_manifest(),'Collection','adult',10)
    assert len(out)==20
    assert out['volunteer_id'].nunique()==10
    assert not out['source_path'].duplicated().any()
    for _,g in out.groupby('volunteer_id'):
        assert set(g['sequence'])=={1,3}
    required={'sample_id','group','original_filename','original_collection','volunteer_id','sequence','source_repository','source_path','source_version','starter_purpose'}
    assert required.issubset(out.columns)


def test_materialize_missing_member_names_path(tmp_path):
    manifest=synthetic_manifest().iloc[:2].copy()
    manifest.loc[0,'filepath']='Collection/missing.jpg'
    zpath=tmp_path/'src.zip'
    root='Repo-main/'
    with zipfile.ZipFile(zpath,'w') as z:
        z.writestr(root+'metadata/manifest.csv', manifest.to_csv(index=False))
        z.writestr(root+manifest.iloc[1].filepath, b'notreal')
    with pytest.raises(FileNotFoundError, match='Collection/missing.jpg'):
        materialize_samples(zpath,tmp_path/'out', adult_collection='Collection', pediatric_collection='Collection', volunteers=1)
