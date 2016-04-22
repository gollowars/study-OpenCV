import numpy as np
import cv2

r = 0
g = 0
b = 255

width = 480
height = 360
pixel = np.array([b,g,r],np.uint8)
wGrid = np.array([pixel]*width,np.uint8)
newImg = np.array([wGrid]*height,np.uint8)

cv2.imshow('generate img',newImg)
cv2.imwrite('createimg.png',newImg)
cv2.waitKey(0)
