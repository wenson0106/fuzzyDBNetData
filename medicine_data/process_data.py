import cv2 
import os
img_dir = './'
combine = []
for i in range os.listdir(img_dir):
    if '.jpg' in i:
        img = cv2.imread(i)
        resize = cv2.resize()
