import os

class_names = sorted(os.listdir("dataset/train")) 
x=[]

with open('word_list.txt','r') as f:
    for i in f:
        x.append(i)
    y='\n'.join(x)

print(y.split())