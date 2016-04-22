# -*- coding: utf-8 -*-
import cv2
import numpy as np
original = cv2.imread('sample.png', 1)
img = original.copy()
dst = np.zeros(img.shape,np.uint8)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

colorRange = [0,10]
thanSaturate = 0
thanValue = 0

for x in xrange(0,img.shape[1]):
  for y in xrange(0,img.shape[0]):
    # HSV
    if hsv[y,x][0] >= colorRange[0] and hsv[y,x][0] < colorRange[1] and hsv[y,x][1] > thanSaturate and hsv[y,x][2] > thanValue:
      radius = 1
      color = tuple([255,0,0])
      thicness = 1
      cv2.circle(img,tuple([x,y]),radius,color,thicness)

      dst[y,x] = img[y,x]

cv2.imshow('Original',original)
cv2.imshow('Add',img)
cv2.imshow('Diff',dst)
cv2.imwrite('add.png',img)
cv2.imwrite('diff.png',dst)
cv2.waitKey(0)