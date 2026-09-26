from __future__ import annotations
import os
from typing import Any
import numpy as np
from PIL import Image


def pretrained_demo_available() -> tuple[bool,str]:
    try:
        import torch  # noqa: F401
        import torchvision  # noqa: F401
        return True, 'PyTorch and torchvision are available.'
    except Exception as exc:
        return False, f'PyTorch/torchvision unavailable: {exc}'


def _pil_to_tensor(image: Image.Image):
    from torchvision.transforms.functional import to_tensor
    return to_tensor(image.convert('RGB'))


def load_generic_maskrcnn(download_weights: bool=True):
    if os.getenv('ORALHEALTH_SKIP_MODEL_DOWNLOAD') == '1' and download_weights:
        raise RuntimeError(
            'Model download skipped. This is a generic COCO-pretrained demonstration, not a dental model. '
            'Unset ORALHEALTH_SKIP_MODEL_DOWNLOAD to rerun with downloaded weights.'
        )
    ok,msg=pretrained_demo_available()
    if not ok:
        raise RuntimeError(msg)
    from torchvision.models.detection import maskrcnn_resnet50_fpn
    model=maskrcnn_resnet50_fpn(weights='DEFAULT' if download_weights else None)
    model.eval()
    return model


def predict_generic_instances(model, image: Image.Image, score_threshold: float=.5) -> dict[str,Any]:
    tensor=_pil_to_tensor(image)
    try:
        import torch
        with torch.no_grad():
            pred=model([tensor])[0]
    except Exception:
        pred=model([tensor])[0]
    scores=pred['scores'].detach().cpu().numpy()
    keep=scores>=score_threshold
    masks=pred['masks'].detach().cpu().numpy()[keep]
    if masks.ndim==4 and masks.shape[1]==1:
        masks=masks[:,0]
    return {
        'boxes':pred['boxes'].detach().cpu().numpy()[keep],
        'labels':pred['labels'].detach().cpu().numpy()[keep],
        'scores':scores[keep],
        'masks':masks,
    }
