import cv2
from pathlib import Path
from typing import Union
import numpy as np

def preprocess_image(image_path: Union[str, Path]) -> np.ndarray:
    """Preprocess a handwritten image for recognition."""
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Failed to load image at {image_path}")
    _,binary=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
    img=cv2.bitwise_not(binary)
    img=cv2.resize(img,(64,64))/255.0
    img=img.reshape(1, 64, 64, 1)
    

    return img
