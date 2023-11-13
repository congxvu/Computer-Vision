import math
import numpy as np
import cv2
import os

path = 'C:/Users/congx/OneDrive/Documents/PS1-master/pics'

image1 = cv2.imread('dog.bmp')
image2= cv2.imread('cat.bmp')

cutoff_frequency = 7

filter = cv2.getGaussianKernel(ksize=cutoff_frequency*4+1, sigma=cutoff_frequency)
filter = np.dot(filter, filter.T)
    
low_frequencies = cv2.filter2D(image1,-1,filter)

high_frequencies = image2 - cv2.filter2D(image2,-1,filter)

temp_image = low_frequencies + high_frequencies

cv2.imwrite(os.path.join(path ,'ps1-7-a-1.png'), temp_image)

cv2.imshow('Result', temp_image)


cv2.waitKey(0)