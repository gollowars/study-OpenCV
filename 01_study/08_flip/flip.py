# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('sample.png')
rimg = img.copy()
fimg = img.copy()
rimg = cv2.flip(img,1)
fimg = cv2.flip(img,0)

cv2.imshow('Original',img)
cv2.imshow('Vertical',rimg)
cv2.imshow('Horizontal',fimg)

cv2.imwrite('flip-vertical.png',rimg)
cv2.imwrite('flip-horizontal.png',fimg)


cv2.waitKey(0)
cv2.destroyAllWindows()