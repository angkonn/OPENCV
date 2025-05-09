import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring an image
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', blur)

cv.waitKey(0)