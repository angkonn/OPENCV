# A histogram is a graphical representation of the distribution of pixel intensities in an image, showing how many pixels have each intensity value. It’s used to analyze image brightness, contrast, and color distribution for tasks like enhancement or thresholding.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')



mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255,-1)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('Mask', masked)

#histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    clr_hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(clr_hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)








