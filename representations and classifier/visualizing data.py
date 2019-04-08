# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 02:37:32 2019

@author: mohamed nabil
"""

import cv2 
import helpers

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

IMAGE_LIST = helpers.load_dataset(image_dir_training)

image_index = 0
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]