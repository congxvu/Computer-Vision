import cv2
import numpy as np

#read image
src = cv2.imread('rose.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract red channel
red_channel = src[:,:,2]

# create empty image with same shape as that of src image
red_img = np.zeros(src.shape)

#assign the red channel of src to empty image
red_img[:,:,2] = red_channel

#save image
cv2.imwrite('rose2.jpg',red_img) 