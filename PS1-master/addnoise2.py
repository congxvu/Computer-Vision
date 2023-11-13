import math
import numpy as np
import cv2
import os

# add image
img1 = cv2.imread('ps1-1-a-1.png')

# coppy image with float 64
image = img1.astype('float64')

# green_channel = 1
# blue channel = 0
channel = 1

sigma = float(64)

# generate random Gaussian noise
G_noise = np.random.randn(*image.shape) * sigma
    
# add noise to specific channel
image[:, :, channel] += G_noise[:, :, channel]
    
# path
path = 'C:/Users/congx/OneDrive/Documents/PS1-master/pics'

# Green channel
cv2.imwrite(os.path.join(path ,'ps1-5-a-1.png'), image)

# Blue channel
#cv2.imwrite(os.path.join(path ,'ps1-5-b-1.png'), image)


#return temp_image

cv2.imshow('temp',image)
#cv2.imshow('noisy_green',noisy_green)
#cv2.imshow('Green Channel',green_channel)
cv2.waitKey(0)