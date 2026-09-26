from __future__ import annotations
from pathlib import Path
import pandas as pd
import yaml
from PIL import Image, UnidentifiedImageError


def load_config(path: str | Path) -> dict:
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Config file not found: {p}')
    with p.open('r',encoding='utf-8') as f:
        data=yaml.safe_load(f) or {}
    if 'dataset' not in data:
        raise ValueError("Config must contain a 'dataset' section")
    return data


def resolve_image_paths(df: pd.DataFrame, image_dir: str | Path) -> pd.DataFrame:
    if 'sample_filename' not in df.columns:
        raise ValueError("Metadata must contain 'sample_filename' for local image resolution")
    out=df.copy()
    base=Path(image_dir)
    out['image_path']=[str(base/name) for name in out['sample_filename']]
    return out


def load_rgb_image(path: str | Path) -> Image.Image:
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Image file not found: {p}')
    try:
        with Image.open(p) as im:
            return im.convert('RGB').copy()
    except UnidentifiedImageError as exc:
        raise ValueError(f'Image could not be decoded: {p}') from exc


def dataset_integrity_report(df: pd.DataFrame) -> pd.DataFrame:
    if 'image_path' not in df.columns:
        raise ValueError("DataFrame must contain 'image_path'; call resolve_image_paths first")
    rows=[]
    for row in df.itertuples(index=False):
        p=Path(row.image_path)
        status='ok'; detail=''
        if not p.exists():
            status='missing'; detail='file does not exist'
        else:
            try:
                with Image.open(p) as im:
                    im.verify()
            except Exception as exc:
                status='corrupt'; detail=str(exc)
        rows.append({'sample_id':row.sample_id,'image_path':str(p),'status':status,'detail':detail})
    return pd.DataFrame(rows)
