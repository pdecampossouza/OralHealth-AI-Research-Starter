from __future__ import annotations
import numpy as np
import pandas as pd


def assert_no_subject_overlap(splits: dict[str,pd.DataFrame], subject_col: str='volunteer_id') -> None:
    names=list(splits)
    sets={k:set(v[subject_col].tolist()) for k,v in splits.items()}
    for i,a in enumerate(names):
        for b in names[i+1:]:
            overlap=sets[a]&sets[b]
            if overlap:
                vals=', '.join(map(str,sorted(overlap)))
                raise ValueError(f'Subject overlap detected for {vals} between {a} and {b}')


def subject_split(df: pd.DataFrame, subject_col: str='volunteer_id', train_size: float=.6, val_size: float=.2, test_size: float=.2, random_state: int=42) -> dict[str,pd.DataFrame]:
    if not np.isclose(train_size+val_size+test_size,1.0):
        raise ValueError('Split fractions must sum to 1.0')
    subjects=np.array(sorted(df[subject_col].dropna().unique()))
    if len(subjects)<3:
        raise ValueError('Need at least three distinct subjects')
    rng=np.random.default_rng(random_state); rng.shuffle(subjects)
    n=len(subjects); n_train=int(round(n*train_size)); n_val=int(round(n*val_size))
    if n_train<1: n_train=1
    if n_val<1: n_val=1
    if n_train+n_val>=n: n_train=max(1,n-2); n_val=1
    train=set(subjects[:n_train]); val=set(subjects[n_train:n_train+n_val]); test=set(subjects[n_train+n_val:])
    splits={
        'train':df[df[subject_col].isin(train)].copy(),
        'validation':df[df[subject_col].isin(val)].copy(),
        'test':df[df[subject_col].isin(test)].copy(),
    }
    assert_no_subject_overlap(splits,subject_col)
    return splits


def split_summary(splits: dict[str,pd.DataFrame], subject_col: str='volunteer_id') -> pd.DataFrame:
    return pd.DataFrame([{'split':k,'rows':len(v),'subjects':v[subject_col].nunique()} for k,v in splits.items()])
