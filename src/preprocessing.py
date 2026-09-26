from __future__ import annotations
import cv2
import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image.ndim==2:
        return image.copy()
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def gaussian_blur(image: np.ndarray, kernel_size: int=5) -> np.ndarray:
    if kernel_size%2==0 or kernel_size<1:
        raise ValueError('kernel_size must be a positive odd integer')
    return cv2.GaussianBlur(image,(kernel_size,kernel_size),0)


def canny_edges(image: np.ndarray, low: int=50, high: int=150) -> np.ndarray:
    gray=to_grayscale(image)
    return cv2.Canny(gray,low,high)


def sobel_edges(image: np.ndarray) -> np.ndarray:
    gray=to_grayscale(image).astype(np.float32)
    gx=cv2.Sobel(gray,cv2.CV_32F,1,0,ksize=3); gy=cv2.Sobel(gray,cv2.CV_32F,0,1,ksize=3)
    return cv2.magnitude(gx,gy).astype(np.float32)


def otsu_threshold(image: np.ndarray) -> np.ndarray:
    gray=to_grayscale(image)
    _,out=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return out
