import math
import numpy as np
import cv2

#% Inspect image values
img1 = cv2.imread('ps1-1-a-1.png')
img = img1.copy()
#green_channel = img[:,:,2]
green_channel = img[:,:,1]
temp_image = np.zeros(img.shape, np.uint8)
temp_image = np.copy(green_channel)


#return temp_image

cv2.imshow('temp',temp_image)
cv2.imshow('original',img)
cv2.waitKey(0)