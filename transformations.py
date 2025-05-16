import cv2 as cv

img = cv.imread('Photos/boston.png')

cv.imshow('Boston',img)

cv.waitKey(0)