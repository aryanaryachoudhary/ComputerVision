#Joining Images 

import cv2
import numpy as np

img = cv2.imread("Resources/barack.jpg")

imghor = np.hstack((img,img))
imgver = np.vstack((img,img))

cv2.imshow("Horizontal Image",imghor)
cv2.imshow("Vertical Image",imgver)

cv2.waitKey(0)