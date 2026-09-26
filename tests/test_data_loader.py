from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from PIL import Image

from src.data_loader import load_config, load_rgb_image, resolve_image_paths, dataset_integrity_report
from src.metadata import load_metadata, validate_metadata

REQUIRED=['sample_id','group','original_filename','original_collection','volunteer_id','source_repository','source_path','source_version','starter_purpose']


def make_meta(tmp_path, filename='x.png'):
    row={k:'x' for k in REQUIRED}
    row['volunteer_id']=1
    row['sample_id']='s1'; row['group']='adult'; row['sample_filename']=filename
    return pd.DataFrame([row])


def test_config_metadata_and_rgb_loading(tmp_path):
    cfg=tmp_path/'cfg.yaml'; cfg.write_text('dataset:\n  image_dir: images\n  metadata: meta.csv\n', encoding='utf-8')
    assert load_config(cfg)['dataset']['image_dir']=='images'
    df=make_meta(tmp_path)
    meta=tmp_path/'meta.csv'; df.to_csv(meta,index=False)
    loaded=load_metadata(meta); validate_metadata(loaded)
    images=tmp_path/'images'; images.mkdir(); Image.new('L',(4,3),120).save(images/'x.png')
    resolved=resolve_image_paths(loaded,images)
    assert resolved.loc[0,'image_path'].endswith('x.png')
    assert load_rgb_image(resolved.loc[0,'image_path']).mode=='RGB'


def test_missing_config_and_columns_are_actionable(tmp_path):
    with pytest.raises(FileNotFoundError, match='missing.yaml'):
        load_config(tmp_path/'missing.yaml')
    with pytest.raises(ValueError, match='source_version'):
        validate_metadata(pd.DataFrame({'sample_id':['x']}))


def test_integrity_report_names_missing_and_corrupt_files(tmp_path):
    images=tmp_path/'images'; images.mkdir()
    (images/'bad.png').write_bytes(b'not an image')
    df=pd.concat([make_meta(tmp_path,'missing.png'),make_meta(tmp_path,'bad.png')],ignore_index=True)
    df.loc[1,'sample_id']='s2'
    df=resolve_image_paths(df,images)
    report=dataset_integrity_report(df)
    statuses=dict(zip(report.sample_id,report.status))
    assert statuses['s1']=='missing'
    assert statuses['s2']=='corrupt'
    assert 'missing.png' in report.loc[report.sample_id.eq('s1'),'image_path'].iloc[0]


def test_custom_filenames_work_without_source_filename_parsing(tmp_path):
    images=tmp_path/'arbitrary'; images.mkdir(); Image.new('RGB',(2,2)).save(images/'anything-name.png')
    df=make_meta(tmp_path,'anything-name.png')
    validate_metadata(df)
    resolved=resolve_image_paths(df,images)
    assert dataset_integrity_report(resolved).status.tolist()==['ok']
