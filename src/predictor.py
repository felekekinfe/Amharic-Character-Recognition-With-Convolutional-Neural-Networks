from tensorflow.keras.models import load_model
from preprocessing import preprocess_image
import numpy as np
import os
import cv2

def predictor(img_path,class_names):

    
    if img_path is None:
        return 'image not found'
    try:
        cnn_model=load_model('amharic_cnn.h5')

    except FileNotFoundError:
        raise('cant find the model')
    img=preprocess_image(img_path)
    #img=cv2.bitwise_not(img)


    predictions=cnn_model.predict(img)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class = class_names[predicted_class_idx]
    
    print(f"Predicted Amharic character {img_path}: {predicted_class}")
    return predicted_class

if __name__=='__main__':
    
    # img_path='dataset/train'
    # class_names = sorted(os.listdir("dataset/train"))  

    # for img in os.listdir(img_path):
    #     print(img)
    #     impath=os.path.join(img_path,img)
    #     for i in os.listdir(impath):
    #         im=os.path.join(impath,i)


    #         x=predictor(im,class_names)
    #         if str(x)==str(img):
    #             r+=1
    #         else:
    #             w+=1
    print(f'right: {r} /nwrong: {w}')  
    # x=predictor('dataset/train/ሜ/026my.67.jpg',class_names)
    # print(x)
        
