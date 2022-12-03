#FACE DETECTION AND CROPPING CODE
import numpy as np
import cv2 
import matplotlib.pyplot as plt
%matplotlib inline
!pip install facenet-pytorch
from facenet_pytorch import MTCNN
mtcnn = MTCNN()
#lOAD THE VIDEO
from PIL import Image
import os
print(os.getcwd())
num_files = list(range(1000))
path = 'C:/Users/Ridwan Bello/Desktop/Dataset/RIDWAN UI/UI'
save_paths = save_path = [f'face2_{i}.jpg' for i in range(len(num_files))]
for file_, newpath in zip(sorted(os.listdir(path)), save_paths):
    if file_[-1] == 'g':
        im = Image.open(path+'/'+file_)
        mtcnn(im, save_path=newpath)
        
