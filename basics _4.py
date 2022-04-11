#croping single persons image from multiple faces
#https://youtu.be/WQeoO7MI0Bs?t=3017
import cv2
import numpy as np

img = cv2.imread("cards1.jpg")

width,height = 250,350
pts1 = np.float32([[368,680],[887,591],[491,1449],[1069,1322]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("cards",img)
cv2.imshow("outPut",imgOutput)

cv2.waitKey(0)