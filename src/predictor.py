from tensorflow.keras.models import load_model
from preprocessing import preprocess_image
import numpy as np
import os

def predictor(img_path,class_names):

    
    if img_path is None:
        return 'image not found'
    try:
        cnn_model=load_model('amharic_cnn.h5')

    except FileNotFoundError:
        raise('cant find the model')
    img=preprocess_image(img_path)

    predictions=cnn_model.predict(img)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class = class_names[predicted_class_idx]
    
    print(f"Predicted Amharic character: {predicted_class}")
    return predicted_class

if __name__=='__main__':
    img_path='dataset/te/ሀ/ሀ_1.png'
   
    class_names = sorted(os.listdir("dataset/test"))  # e.g., ["ሀ", "ሁ", "ሂ", ...]

    # Predictg"
    
    x=predictor(img_path,class_names)
    print(x)
        
