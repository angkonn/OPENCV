# A histogram is a graphical representation of the distribution of pixel intensities in an image, showing how many pixels have each intensity value. It’s used to analyze image brightness, contrast, and color distribution for tasks like enhancement or thresholding.

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey Image", gray)


# Grayscale histogram
gray_hist

cv.waitKey(0)