import os
import numpy as np
import pytest
from PIL import Image
from src.visualization import make_image_grid, overlay_binary_mask, draw_boxes, save_prediction_artifact


def test_grid_overlay_boxes_and_save(tmp_path):
    imgs=[Image.new('RGB',(20,10),'white') for _ in range(3)]
    fig=make_image_grid(imgs,['a','b','c'],columns=2)
    assert len(fig.axes)>=3
    mask=np.zeros((10,20),dtype=bool); mask[:,5:10]=1
    over=overlay_binary_mask(imgs[0],mask); assert over.size==imgs[0].size
    boxed=draw_boxes(imgs[0],[[1,1,10,8]],['x']); assert boxed.size==imgs[0].size
    out=save_prediction_artifact(boxed,tmp_path/'nested'/'x.png'); assert out.exists()


def test_save_error_contains_target(monkeypatch,tmp_path):
    target=tmp_path/'x.png'
    def boom(self,*args,**kwargs):
        raise OSError('denied')
    monkeypatch.setattr(Image.Image,'save',boom)
    with pytest.raises(OSError,match='x.png'):
        save_prediction_artifact(Image.new('RGB',(2,2)),target)
