import cv2 as cv
# Imports the OpenCV library, a powerful tool for image processing and computer vision, aliased as 'cv' for convenience.

import numpy as np
# Imports NumPy, a library for numerical operations, essential for handling image data as arrays.

img = cv.imread('Photos/cats.jpg')
# Loads the image 'cats.jpg' from the 'Photos' directory into a NumPy array in BGR format.

blank = np.zeros(img.shape, dtype='uint8')
# Creates a blank (black) image with the same dimensions as 'img', using 8-bit unsigned integers (0-255) for pixel values.

cv.imshow('Blank', blank)
# Displays the blank image in a window titled 'Blank'; initially, it appears completely black.

cv.imshow('Cats', img)
# Displays the original image in a window titled 'Cats' for visualization.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Converts the BGR image to grayscale, reducing it to a single channel for simpler processing.

cv.imshow('Gray', gray)
# Displays the grayscale image in a window titled 'Gray' to show the conversion result.

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# Applies a 5x5 Gaussian blur to the grayscale image to reduce noise, using default border handling.

cv.imshow('Blur', blur)
# Displays the blurred image in a window titled 'Blur' for illustrative purposes.

canny = cv.Canny(img, 125, 175)
# Detects edges in the original image using the Canny algorithm, with thresholds 125 and 175 to filter edge strength.

cv.imshow('Canny edges', canny)
# Displays the edge-detected image in a window titled 'Canny edges', showing white edges on a black background.

ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY_INV)
# Applies inverse binary thresholding to the Canny image, inverting it so edges become black on a white background.

cv.imshow('Thresh', thresh)
# Displays the thresholded (inverted) image in a window titled 'Thresh'.

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Finds contours (boundaries) of black regions in the thresholded image, using a simple approximation method.

print(f'{len(contours)} contours found!')
# Prints the total number of contours detected in the image.

cv.drawContours(blank, contours, -1, (0,0,255), 1)
# Draws all detected contours on the blank image in red (BGR: 0,0,255) with a thickness of 1 pixel.

cv.imshow('Countours Drawn', blank)
# Displays the blank image with red contours in a window titled 'Countours Drawn'.

cv.waitKey(0)
# Waits indefinitely for a key press, keeping all windows open until the user closes the program.