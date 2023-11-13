import math
import numpy as np
import cv2
import os

path = 'C:/Users/congx/OneDrive/Documents/PS1-master/pics'

#% Inspect image values
img1 = cv2.imread('ps1-1-a-1.png')
img2 = cv2.imread('ps1-1-a-2.png')

# extract green channel from image
green_channel = img1[:,:,1]
img1_green = green_channel

# shift green
shift = 2
shift_green =cv2.copyMakeBorder(img1_green[:, shift:], 0, 0, 0, shift, cv2.BORDER_REPLICATE)

temp_img1 = green_channel.astype('float64')
temp_img2 = shift_green.astype('float64')

# subtract 2 images
temp_diff = temp_img1 - temp_img2
    
# read images value
min_value = float(np.min(temp_diff))
max_value = float(np.max(temp_diff))

    
# find distance
distance = max_value - min_value
distance = distance or float(distance)
    
temp_image = (temp_diff - min_value) * np.divide(255, distance)
    
# convert image NaN to 0
temp_image[np.isnan(temp_image)] = 0


cv2.imwrite(os.path.join(path ,'ps1-4-d-1.png'), temp_image)

#cv2.imshow('Result', temp_img)


cv2.waitKey(0)