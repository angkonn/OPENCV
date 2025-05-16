# countours -> Boundaries of an object 
import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

cv.waitKey(0)