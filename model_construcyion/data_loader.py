import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical

class DataLoader:
    """Loads and preprocesses Amharic character images from a folder structure."""
    
    def __init__(self, data_dir, img_size=(64, 64)):
        """Initialize the DataLoader with directory and image size.

        Args:
            data_dir (str): Path to data directory (e.g., 'dataset/train').
            img_size (tuple): Target image size (height, width), default (64, 64).
        """
        self.data_dir = data_dir
        self.img_size = img_size
        self.classes = sorted(os.listdir(data_dir))
        self.num_classes = len(self.classes)
        self.class_to_idx = {cls: idx for idx, cls in enumerate(self.classes)}

    def load_data(self):
        """Load and preprocess images and labels from folder structure.

        Returns:
            tuple: (images, labels) where images is a numpy array of shape
                (samples, 64, 64, 1) and labels is one-hot encoded array of shape
                (samples, num_classes).
        """
        images = []
        labels = []
        
        for class_name in self.classes:
            class_dir = os.path.join(self.data_dir, class_name)
            for img_name in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                _,binary=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
                img=cv2.bitwise_not(binary)
                img = cv2.resize(img, self.img_size)
                images.append(img)
                labels.append(self.class_to_idx[class_name])
        
        images = np.array(images).reshape(-1, 64, 64, 1) / 255.0
        labels = to_categorical(labels, self.num_classes)
        return images, labels
    def custom_processing_for_datagen(self,img):
        img=(img*255).astype(np.uint8)
        img=cv2.bitwise_not(img)

        if np.random.ran()>0.5:
            noise=np.random(0,25,img.shape)
            img=img+noise
            img=np.clip(img,0,255)
        img=img.astype(np.float32)/255.0
        return img

    def get_datagen(self):
        """Create a data augmentation generator for training.

        Returns:
            ImageDataGenerator: Configured generator for image augmentation.
        """
        return ImageDataGenerator(
            rotation_range=10,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=10,
            zoom_range=0.1,
            fill_mode='nearest',
            rescale=1/255,
            preprocessing_function=self.custom_processing_for_datagen
        )