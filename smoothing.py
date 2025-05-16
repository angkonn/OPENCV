import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


# Averaging
average = cv.blur(img, (5,5))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (5,5),0)
cv.imshow('Gaussian Blur',gaussian)

cv.waitKey(0)