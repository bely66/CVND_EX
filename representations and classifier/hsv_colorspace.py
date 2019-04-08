# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 02:15:07 2019

@author: mohamed nabil
"""
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

image = cv2.imread('images/water_balloons.jpg')
im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
im_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

r = im_rgb[:,:,0]
g = im_rgb[:,:,1]
b = im_rgb[:,:,2]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))

ax1.set_title('Red')
ax1.imshow(r, cmap='gray')

ax2.set_title('Green')
ax2.imshow(g, cmap='gray')

ax3.set_title('Blue')
ax3.imshow(b, cmap='gray')

h = im_hsv[:,:,0]
s= im_hsv[:,:,1]
v = im_hsv[:,:,2]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))

ax1.set_title('Red')
ax1.imshow(h, cmap='gray')

ax2.set_title('Green')
ax2.imshow(s, cmap='gray')

ax3.set_title('Blue')
ax3.imshow(v, cmap='gray')


#pink bounds 
low = np.array([160,0,0])
high = np.array([180,200,255])

mask = cv2.inRange(im_hsv,low,high)
plt.imshow(mask,cmap='gray')
im_hsv[mask==0]=[0,0,0]
im = cv2.cvtColor(im_hsv,cv2.COLOR_HSV2RGB)
plt.imshow(im)
