# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

###
# 画素へのアクセス
###
 
#イメージ生成
image = cv2.imread('sample.png')

x = 200
y = 180
width = 150
height = 120

dstImg = image[y:y+height,x:x+width]

cv2.imshow('image',image)
cv2.imshow('dst',dstImg)

cv2.imwrite('trimming.png',dstImg)
cv2.waitKey(0)
