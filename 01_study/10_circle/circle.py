import cv2
import numpy as np

img = cv2.imread('sample.png')
w = 400
h = 300

plane = np.zeros([300,500],np.uint8)
center = tuple([plane.shape[1]/2,plane.shape[0]/2])
radius = 100
color = tuple([255,0,0])
thickness = 2
cv2.circle(plane,center,radius,color,thickness)
cv2.imshow('plane',plane)
cv2.imwrite('circle.png',plane)
cv2.waitKey(0)