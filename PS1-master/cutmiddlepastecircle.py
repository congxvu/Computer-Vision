import math
import numpy as np
import cv2

#% Inspect image values
img_d = cv2.imread('ps1-1-a-1.png')
img_r = cv2.imread('ps1-1-a-2.png')

src = img_r
dst = img_d

radius = 50

src_height = src.shape[0]
src_width = src.shape[1]
 
# Center of src image
y_src = src.shape[0]//2	# height of src image
x_src = src.shape[1]//2	# width

# Center of dst image
y_dst = dst.shape[0]//2	# height of dst image
x_dst = dst.shape[1]//2	# width

# Make a copy dst to temp_image
temp_image = dst.copy()

# Find all pixels within the radius at src image and then copy to dst image
for x in range(src_width):
    for y in range(src_height):
        # find distance from the center
        distance = math.sqrt((x - x_src)**2 + (y - y_src)**2)
        # copy pixel from src to dst if (x,y) within the circle
        if distance <= radius:
            dx = x_dst + (x - x_src) + 2
            dy = y_dst + (y - y_src) + 2
            temp_image[dy, dx] = src[y, x]


#return temp_image

cv2.imshow('temp',temp_image)
cv2.waitKey(0)