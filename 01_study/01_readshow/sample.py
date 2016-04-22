# -*- coding: utf-8 -*-
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample.png')

cv2.imshow('result',img)
cv2.waitKey(0)