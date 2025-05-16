import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.png')

cv.imshow('Boston',img)

# translation (shifting the image along the x and y axis)
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
cv.imshow('Translated Image', translated)

cv.waitKey(0)