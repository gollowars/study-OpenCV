# -*- coding: utf-8 -*-
import cv2
import numpy as np
src = cv2.imread('sample.png', 1)

dst = np.zeros(src.shape, dtype=np.uint8)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)  #BGR→HSVへ変換

print dst.shape

ij_index = [-1, -1]

max_h = -1
for i in range (dst.shape[0]):
    for j in range (dst.shape[1]):
        if (dst[i,j][0] <20 and dst[i,j][0] > 0 and dst[i,j][1] > 100):
            max_h = dst[i,j][0]
            cv2.circle(src,(j, i),5,(255,0,0),1)
cv2.circle(src,(0, 0),5,(0,0,255),1)
cv2.circle(src,(0, 100),5,(0,0,255),1)
cv2.circle(src,(100, 100),5,(0,0,255),1)
        # print dst[i,j]
print max_h
# x = 110
# y = 148
# print dst[x,y]
# print dst[0, 0]

# cv2.circle(src,(x, y),5,(255,0,0),1)
cv2.imshow('result',src)
cv2.imwrite("output.jpg", src); 
cv2.waitKey(0)