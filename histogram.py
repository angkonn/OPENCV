# A histogram is a graphical representation of the distribution of pixel intensities in an image, showing how many pixels have each intensity value. It’s used to analyze image brightness, contrast, and color distribution for tasks like enhancement or thresholding.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey Image", gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255,-1)

mask = cv.bitwise_and(gray,gray, mask=circle)
cv.imshow('Mask', mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
# the bins parameter (specified as [256] in the code) determines the number of discrete intervals (or "bins") used to group pixel intensity values when computing the histogram.

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()




cv.waitKey(0)