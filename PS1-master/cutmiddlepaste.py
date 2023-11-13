import math
import numpy as np
import cv2

#% Inspect image values
img_d = cv2.imread('ps1-1-a-1.png')
img_r = cv2.imread('ps1-1-a-2.png')

src = img_r
dst = img_d

# Height and width of copied area
h_rect = 100
w_rect = 100
    
# Location of coppied image
y_src = src.shape[0]	# height of src image
x_src = src.shape[1]	# width

cs1 = int(x_src/2 - w_rect/2)
cs2 = int(x_src/2 + w_rect/2)
rs1 = int(y_src/2 - h_rect/2)
rs2 = int(y_src/2 + h_rect/2)

# area is coppied
img2 = src[rs1 : rs2 , cs1 : cs2]


# Location of pasted image
y_dst = dst.shape[0]	# height of dst image
x_dst = dst.shape[1]	# width

cd1 = int(x_dst/2 - w_rect/2)
cd2 = int(x_dst/2 + w_rect/2)
rd1 = int(y_dst/2 - h_rect/2)
rd2 = int(y_dst/2 + h_rect/2)
# copy image in mask area

temp_image = np.copy(dst)
temp_image[rd1 : rd2 , cd1 : cd2] = img2

#cv2.imshow('result',img2)

cv2.imshow('temp',temp_image)

cv2.waitKey()