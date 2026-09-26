from __future__ import annotations
from collections.abc import Mapping, Sequence
from pathlib import Path
import csv
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def iou_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    a=np.asarray(y_true,dtype=bool); b=np.asarray(y_pred,dtype=bool)
    union=np.logical_or(a,b).sum()
    if union==0: return 1.0
    return float(np.logical_and(a,b).sum()/union)


def dice_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    a=np.asarray(y_true,dtype=bool); b=np.asarray(y_pred,dtype=bool)
    denom=a.sum()+b.sum()
    if denom==0: return 1.0
    return float(2*np.logical_and(a,b).sum()/denom)


def instance_count_error(true_count: int, pred_count: int) -> int:
    return abs(int(true_count)-int(pred_count))


def classification_metrics(y_true: Sequence, y_pred: Sequence) -> dict[str,float]:
    return {
        'accuracy':float(accuracy_score(y_true,y_pred)),
        'precision':float(precision_score(y_true,y_pred,average='weighted',zero_division=0)),
        'recall':float(recall_score(y_true,y_pred,average='weighted',zero_division=0)),
        'f1':float(f1_score(y_true,y_pred,average='weighted',zero_division=0)),
    }


def export_results(rows: Sequence[Mapping], path: str | Path) -> Path:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    rows=list(rows)
    if not rows:
        p.write_text('',encoding='utf-8'); return p
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    return p
