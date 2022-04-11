import cv2 
import numpy as np

#print("you__ is small")


img = cv2.imread("ranveer-k.jpg")
kernel = np.ones((5,5),np.uint8)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imBlure = cv2.GaussianBlur(imgray,(9,9),0)
imgcanny = cv2.Canny(img,150,300)
imgDialation = cv2.dilate(imgcanny,kernel,iterations=1)
imgEeoded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("output",imgray)
cv2.imshow("goput",imBlure)
cv2.imshow("canny put",imgcanny)
cv2.imshow("Dialation put",imgDialation)
cv2.imshow("Eeoded put",imgEeoded)
cv2.waitKey(0)

"""cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break"""