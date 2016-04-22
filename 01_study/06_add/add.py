# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

###
# 画素へのアクセス
###
 
#イメージ生成
sample1 = cv2.imread('addsample1.png')
sample2 = cv2.imread('addsample2.png')

width = 300
height = 300

addImg = np.zeros((height,width,3),np.uint8)

for x in xrange(0,width):
  for y in xrange(0,height):
    addpixel = sample1[x,y] + sample2[x,y]
    addImg[x,y] = addpixel


cv2.imshow('add',addImg)
cv2.imwrite('add.png',addImg)
cv2.waitKey(0)