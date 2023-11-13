import cv2
import matplotlib.pyplot as plt

# Crop an image
img = cv2.imread('rose.jpg');
plt.imshow(img);

plt.disp(cv2.size(img));  #% check size

cropped = img[110:310, 10:160];
cv2.imshow(cropped);
cv2.waitKey();