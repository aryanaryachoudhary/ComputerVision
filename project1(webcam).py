from sre_constants import SUCCESS
import cv2

cap = cv2.VideoCapture(0)   #(id of primary webcam)
cap.set(3,640)      #(id of width,dimension)
cap.set(4,480)      #(id of height,dimension)
cap.set(10,100)     #(if for brightness, brightness level)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break