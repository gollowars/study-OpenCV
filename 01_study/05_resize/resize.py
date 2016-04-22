# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

###
# 画素へのアクセス
###
 
#イメージ生成
image = cv2.imread('sample.png')

width = image.shape[0]
height = image.shape[1]
resizeImg = cv2.resize(image,(height/2,width/2))
cv2.imshow('original',image )
cv2.imshow('resize',resizeImg)
cv2.imwrite('resize.png',resizeImg)
cv2.waitKey(0)