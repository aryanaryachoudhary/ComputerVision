#warped perspective

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
width,height = 250,350
pts1 = np.float32([[1030,254],[1300,320],[1212,708],[938,640]])
#I have taken pixels wromg... I'll have to correct that.

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)


