import pandas as pd
import pytest
from src.split_utils import subject_split, assert_no_subject_overlap, split_summary


def frame(n_subjects=10):
    rows=[]
    for s in range(n_subjects):
        rows += [{'volunteer_id':s,'x':1},{'volunteer_id':s,'x':2}]
    return pd.DataFrame(rows)


def test_subject_split_is_deterministic_complete_and_nonoverlapping():
    df=frame()
    a=subject_split(df,random_state=7)
    b=subject_split(df,random_state=7)
    assert {k:set(v.volunteer_id) for k,v in a.items()}=={k:set(v.volunteer_id) for k,v in b.items()}
    assert sum(len(v) for v in a.values())==len(df)
    assert_no_subject_overlap(a)
    counts={k:v.volunteer_id.nunique() for k,v in a.items()}
    assert counts=={'train':6,'validation':2,'test':2}
    summary=split_summary(a)
    assert set(summary['split'])=={'train','validation','test'}


def test_invalid_fractions_and_too_few_subjects():
    with pytest.raises(ValueError,match='sum to 1.0'):
        subject_split(frame(),train_size=.5,val_size=.3,test_size=.3)
    with pytest.raises(ValueError,match='at least three'):
        subject_split(frame(2))


def test_overlap_error_names_subject_and_partitions():
    splits={'train':pd.DataFrame({'volunteer_id':[1]}),'validation':pd.DataFrame({'volunteer_id':[1]}),'test':pd.DataFrame({'volunteer_id':[2]})}
    with pytest.raises(ValueError,match='1.*train.*validation|1.*validation.*train'):
        assert_no_subject_overlap(splits)
