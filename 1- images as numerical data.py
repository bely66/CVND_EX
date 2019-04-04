# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:10:08 2019

@author: USER
"""
import numpy as np 
import cv2 
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
#IMAGE DIRECTORY
direc = 'images\waymo_car.jpg'
#READ THE IMAGE
image = mpimg.imread(direc)
#PUT THE IMAGE IN GRAY
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#PRINT IMAGE SHAPE
print(image.shape)
#PLOT IMAGE USING MATPLOTLIB
plt.imshow(gray, cmap='gray')
print(gray[190,370])
#PRINT MIN AND MAX VALUES AT IMAGE
max_val= np.amax(gray)
min_val = np.amin(gray)
 
print("maximum value = ",max_val)
print("minimum value = ",min_val)
#MAKE A SIMPLE IMAGES USING NUMPY ARRAYS
image_ar = np.array([[15,35,255,120],[12,50,16,23],[180,110,130,155],[10,100,200,150]])
plt.imshow(image_ar,cmap='gray')
