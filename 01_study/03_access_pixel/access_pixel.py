# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

###
# 画素へのアクセス
###

cols = 640
rows = 480
 
#イメージ生成
image = cv2.imread('sample.png')

# print image
print image[0,1]

width = image.shape[0] 
height = image.shape[1]
amount = 2.0

# pixelごといじる。
for x in xrange(0,width):
  for y in xrange(0,height):
    pixel = image[x,y]
    b = pixel[0]
    g = pixel[1]
    r = pixel[2]

    if x < width/2 and y < height/2:
      color = np.array([b,g,r*amount],np.uint8)
    elif x > width/2 and y < height/2:
      color = np.array([b,g*amount,r],np.uint8)
    elif x < width/2 and y > height/2:
      color = np.array([b*amount,g,r],np.uint8)
    else:
      color = np.array([b*amount,g*amount,r*amount],np.uint8)

    image[x,y] = color
    # image[x,y] = color
# image[0:150,0:110] = [0, 255, 128]
cv2.imshow('image',image)
cv2.imwrite('access_pixel.png',image)

cv2.waitKey(0)