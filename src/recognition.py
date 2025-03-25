import cv2
import numpy as np
from tensorflow.keras.models import load_model

try:
    cnn_model=load_model('')
except FileNotFoundError:
    raise FileNotFoundError('cnn model not found')

BASE_UNICODE=0x1200

def recognize_letter(thresh,components):
    characters=[]

    for x,y,w,h in components:
        char_img=thresh[y:y+h,x:x+w]
        char_img=cv2.resize(char_img,(64,64)).reshape(1,64,64,1)/255.0
        pred=cnn_model.predict(char_img)
        letter_idx=np.argmax(pred)
        characters.append(chr(BASE_UNICODE + letter_idx))
    return characters