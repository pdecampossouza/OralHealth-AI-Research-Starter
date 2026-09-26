import os
import numpy as np
import pytest
from PIL import Image

from src.pretrained_demo import load_generic_maskrcnn, predict_generic_instances, pretrained_demo_available

class FakeTensor:
    def __init__(self,a): self.a=np.array(a)
    def detach(self): return self
    def cpu(self): return self
    def numpy(self): return self.a

class FakeModel:
    def eval(self): return self
    def __call__(self,images):
        return [{'boxes':FakeTensor([[1,2,3,4],[5,6,7,8]]),'labels':FakeTensor([1,2]),'scores':FakeTensor([.9,.2]),'masks':FakeTensor(np.ones((2,1,4,4)))}]


def test_prediction_filtering_with_fake_model(monkeypatch):
    monkeypatch.setattr('src.pretrained_demo._pil_to_tensor', lambda im: 'tensor')
    out=predict_generic_instances(FakeModel(),Image.new('RGB',(4,4)),score_threshold=.5)
    assert out['boxes'].shape==(1,4)
    assert out['labels'].tolist()==[1]
    assert out['scores'].tolist()==[.9]
    assert out['masks'].shape==(1,4,4)


def test_skip_mode_blocks_weight_download(monkeypatch):
    monkeypatch.setenv('ORALHEALTH_SKIP_MODEL_DOWNLOAD','1')
    with pytest.raises(RuntimeError,match='generic COCO-pretrained demonstration'):
        load_generic_maskrcnn()


def test_availability_returns_tuple():
    ok,msg=pretrained_demo_available()
    assert isinstance(ok,bool) and isinstance(msg,str)
