# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample.png')

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('result',gray)
cv2.imwrite('grey.png',gray)
cv2.waitKey(0)