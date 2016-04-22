# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('sample.png')

# cv2.imshow('image',img)

width = img.shape[1]
height = img.shape[0]
center = tuple(np.array([width/2, height/2]))
size = tuple(np.array([width,height]))
  
# 回転軸を指定しないafine
# 回転させたい角度
rad = 45*np.pi/180
movX = 10
movY = 10

matrix = [
  [np.cos(rad),-1*np.sin(rad),movX],
  [np.sin(rad),np.cos(rad),movY]
]

afMat = np.float32(matrix)

# 回転軸を指定するafine
angle = 45
scale = 1.0
rotMat = cv2.getRotationMatrix2D(center,angle,scale)

# afnImg = cv2.warpAffine(img,afMat,size,flags=cv2.INTER_LINEAR)
afnImg = cv2.warpAffine(img,rotMat,size,flags=cv2.INTER_CUBIC)
cv2.imshow('affine image',afnImg)
cv2.imwrite('affine.png',afnImg)
cv2.waitKey(0)
cv2.destroyAllWindows()