import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)



# 1. Paint the image a certain color

# blank[:] = 0,255,0
# cv.imshow('Green',blank)

# blank[:] = 0,0,255
# cv.imshow('Red',blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 80, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)
cv.waitKey(0)