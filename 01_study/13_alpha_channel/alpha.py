import numpy as np
import cv2

# img = cv2.imread('lena.jpg')
tin = cv2.imread('tinder.png')

# width = tin.shape[1]
# height = tin.shape[0]

a = tin

r = 0
g = 0
b = 255

width = 480
height = 360
pixel = np.array([b,g,r],np.uint8)
wGrid = np.array([pixel]*width,np.uint8)
newImg = np.array([wGrid]*height,np.uint8)

cv2.imshow('generate img',newImg)
cv2.waitKey(0)

# img[0:height,0:width] = tin

# cv2.imshow('show tin',img)
# cv2.waitKey(0)