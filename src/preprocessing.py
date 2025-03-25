import cv2
from pathlib import Path


def preprocess_image(img_path: Path):
    img=cv2.imread(str(img_path),cv2.IMREAD_GRAYSCALE)
    thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    
    return thresh