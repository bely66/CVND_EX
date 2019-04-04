# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:30:07 2019

@author: USER
"""

import matplotlib.image as pimg
import matplotlib.pyplot as plt

direc = 'images\wa_state_highway.jpg'
image = pimg.imread(direc)
plt.imshow(image)