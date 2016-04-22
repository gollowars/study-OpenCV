import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

img = cv2.imread('sample.png')
bgr = cv2.split(img)

blue = bgr[0]
green = bgr[1]
red = bgr[2]

# plt.add(blue)
# plt.show(blue)

changeChannel = cv2.merge([red,green,blue])

cv2.imshow('changeChannel',changeChannel)
cv2.waitKey(0)