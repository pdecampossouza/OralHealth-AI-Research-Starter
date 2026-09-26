from __future__ import annotations
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = [
    'sample_id','group','original_filename','original_collection','volunteer_id',
    'source_repository','source_path','source_version','starter_purpose'
]

def load_metadata(path: str | Path) -> pd.DataFrame:
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Metadata file not found: {p}')
    return pd.read_csv(p)

def validate_metadata(df: pd.DataFrame) -> None:
    missing=[c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f'Missing required metadata columns: {", ".join(missing)}')
