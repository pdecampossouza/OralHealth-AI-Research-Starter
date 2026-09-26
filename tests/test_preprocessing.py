import numpy as np
from src.preprocessing import to_grayscale, gaussian_blur, canny_edges, sobel_edges, otsu_threshold


def test_preprocessing_shapes_and_binary_outputs():
    img=np.zeros((20,20,3),dtype=np.uint8); img[:,10:]=255
    gray=to_grayscale(img); assert gray.shape==(20,20)
    assert gaussian_blur(gray,5).shape==gray.shape
    c=canny_edges(gray); assert c.shape==gray.shape and set(np.unique(c)).issubset({0,255})
    s=sobel_edges(gray); assert s.shape==gray.shape and s.dtype==np.float32
    o=otsu_threshold(gray); assert set(np.unique(o)).issubset({0,255})
