import cv2
import numpy as np

img = cv2.imread("Resources/barack.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1260,720)) 
                           #(width,height)
imgCropped = img[0:1000,200:720]
                #[height,width]
cv2.imshow("image",img)
cv2.imshow("resized image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)


