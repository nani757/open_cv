#to shapes and texts
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[:]=255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),7)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),7)
cv2.circle(img,(400,50),30,(255,255,0),7)
cv2.putText(img,"OPENCV",(300,300),"""for particular angle""",cv2.FONT_HERSHEY_COMPLEX,1,"""for pogision""",(0,150,0),4)#https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=2054s

cv2.imshow("image",img)
 
cv2.waitKey(0)  