#Face Detection using Webcam
import cv2
from sre_constants import SUCCESS

cap = cv2.VideoCapture(0)   #(id of primary webcam)
cap.set(3,640)      #(id of width,dimension)
cap.set(4,480)      #(id of height,dimension)
cap.set(10,100)     #(if for brightness, brightness level)

while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("FaceCam",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
