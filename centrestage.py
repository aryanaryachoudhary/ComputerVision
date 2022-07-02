import pyvirtualcam
import cv2

cap = cv2.VideoCapture(0)
# cap.set(3,640)      #(id of width,dimension)
# cap.set(4,480)      #(id of height,dimension)
# cap.set(10,100)     #(if for brightness, brightness level)

fmt = pyvirtualcam.PixelFormat.BGR
with pyvirtualcam.Camera(width=1280, height=720, fps=20, fmt = fmt) as cam:
    while True:
        ret_val, frame = cap.read()
        face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
        # body_cascade = cv2.CascadeClassifier("resources/body.xml")

        imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(imgGray,1.1,4)
        # bodies = body_cascade.detectMultiScale(imgGray,1.1,4)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # for(x,y,w,h) in bodies:
        #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.BORDER_DEFAULT)

        cam.send(frame)
        cam.sleep_until_next_frame()
        if cv2.waitKey(1) == 27:
            break  
        
    cv2.destroyAllWindows()