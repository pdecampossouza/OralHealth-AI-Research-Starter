from __future__ import annotations
from collections.abc import Sequence
from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def make_image_grid(images: Sequence[Image.Image], titles: Sequence[str] | None=None, columns: int=4):
    if columns<1: raise ValueError('columns must be >= 1')
    rows=math.ceil(len(images)/columns) if images else 1
    fig,axes=plt.subplots(rows,columns,figsize=(4*columns,3*rows),squeeze=False)
    titles=titles or ['']*len(images)
    for ax in axes.flat: ax.axis('off')
    for i,img in enumerate(images):
        axes.flat[i].imshow(img); axes.flat[i].set_title(titles[i] if i<len(titles) else '')
    fig.tight_layout(); return fig


def overlay_binary_mask(image: Image.Image, mask: np.ndarray, alpha: float=.35) -> Image.Image:
    base=image.convert('RGBA')
    m=np.asarray(mask,dtype=bool)
    if m.shape != (image.height,image.width):
        raise ValueError(f'Mask shape {m.shape} does not match image {(image.height,image.width)}')
    overlay=np.zeros((image.height,image.width,4),dtype=np.uint8)
    overlay[m]=[255,0,0,int(255*alpha)]
    return Image.alpha_composite(base,Image.fromarray(overlay,'RGBA')).convert('RGB')


def draw_boxes(image: Image.Image, boxes: Sequence[Sequence[float]], labels: Sequence[str] | None=None) -> Image.Image:
    out=image.convert('RGB').copy(); d=ImageDraw.Draw(out)
    for i,box in enumerate(boxes):
        d.rectangle(tuple(box),outline='red',width=2)
        if labels and i<len(labels): d.text((box[0],box[1]),str(labels[i]),fill='red')
    return out


def save_prediction_artifact(image: Image.Image, output_path: str | Path) -> Path:
    p=Path(output_path)
    try:
        p.parent.mkdir(parents=True,exist_ok=True)
        image.save(p)
    except OSError as exc:
        raise OSError(f'Could not save prediction artifact to {p}: {exc}') from exc
    return p
