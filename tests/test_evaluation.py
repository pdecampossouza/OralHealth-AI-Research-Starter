import numpy as np
from src.evaluation import iou_score,dice_score,instance_count_error,classification_metrics,export_results


def test_segmentation_metrics_known_values():
    a=np.array([[1,1],[0,0]],bool); b=np.array([[1,0],[1,0]],bool)
    assert abs(iou_score(a,b)-1/3)<1e-9
    assert abs(dice_score(a,b)-.5)<1e-9
    z=np.zeros((2,2),bool); assert iou_score(z,z)==1.0 and dice_score(z,z)==1.0
    assert instance_count_error(5,3)==2


def test_classification_and_export(tmp_path):
    m=classification_metrics([0,1,1],[0,1,0])
    assert {'accuracy','precision','recall','f1'}.issubset(m)
    p=export_results([{'a':1},{'a':2}],tmp_path/'r.csv')
    assert p.exists() and p.read_text().count('\n')>=2
