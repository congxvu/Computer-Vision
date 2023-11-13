import math
import numpy as np
import cv2

#% Inspect image values
img_d = cv2.imread('ps1-1-a-1.png')
img_r = cv2.imread('ps1-1-a-2.png')

src = img_r
dst = img_d

radius = 50
 
# Center of src image
y_src = src.shape[0]//2	# height of src image
x_src = src.shape[1]//2	# width

# Center of dst image
y_dst = dst.shape[0]//2	# height of dst image
x_dst = dst.shape[1]//2	# width

# copy empty image from src image with black background
mask_src = np.zeros_like(src)

# make and fill src circle with full color channels
cir_src = cv2.circle(mask_src, (x_src,y_src), radius, (255,255,255), -1)

# set my output img to zero everywhere except my mask
output_img = src.copy()
output_img[np.where(cir_src==0)] = 0

# cv2.imshow('source circle',output_img)


# copy empty image from dst image with black background
mask_dst = np.zeros_like(dst)

# make and fill src circle with full color channels
cir_dst = cv2.circle(mask_dst, (x_dst,y_dst), radius, (255,255,255), -1)

# set my output img to zero everywhere except my mask
output_img2 = dst.copy()
output_img2[np.where(cir_dst!=0)] = output_img[np.where(cir_src!=0)]

cv2.imshow('dest circle',output_img2)
#cv2.imshow('temp',temp_image)

# allignment 2 circles

#temp_img = output_img + output_img2
#temp_img = cv2.bitwise_and(output_img, output_img2, mask=mask_dst)

#cv2.imshow('Result', temp_img)


cv2.waitKey(0)