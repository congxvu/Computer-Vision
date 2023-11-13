import math
import numpy as np
import cv2

#% Inspect image values
img1 = cv2.imread('ps1-1-a-1.png')

# Make a copy dst to temp_image
temp_image = img1.copy()
# temp_image = img1.astype('float64')

# TODO: Choose a sigma value:
sigma = 16
channel = 1

# process green channel
if channel == 1:
# extract green channel from image
	#green_channel = img1[:,:,1]
	green_channel = temp_image[:,:,1]
	print(green_channel.shape)
	# create noise on blue channel
	noisy_green = np.zeros(temp_image.shape, np.uint8)
	noisy_green = cv2.randn(temp_image.shape,0,sigma)
	print(noisy_green.shape)

temp_image [:,:,1] = noisy_green

#return temp_image

cv2.imshow('temp',noisy_green)
cv2.imshow('temp',temp_image)
cv2.waitKey(0)