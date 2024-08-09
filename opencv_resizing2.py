# resizing
import os
import cv2

# This is my second attempt at resizing this image! I reorganized the code to match the order that the tutorial put it.

# img = cv2.imread(os.path.join('.','samoyed2.jpg'))
# Note: the line above didn't work, so I'm using one that ChatGPT gave me instead. 
img = cv2.imread(os.path.expanduser('~/Documents/coding/data/samoyed2.jpeg'))
# Original image size: (691, 563)
resized_img = cv2.resize(img, (int(281.5), int(345.5))) # I also got rid of the int() function here! 

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
