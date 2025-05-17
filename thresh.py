import cv2 as cv
# Imports the OpenCV library, aliased as 'cv', for image processing tasks like reading, displaying, and transforming images.

img = cv.imread('Photos/cats.jpg')
# Loads the color image 'cats.jpg' from the 'Photos' folder into the variable 'img' as a BGR (Blue, Green, Red) image.

cv.imshow('Cats', img)
# Displays the color image in a window named 'Cats'.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Converts the color image 'img' from BGR to grayscale, storing the result in 'gray'. Grayscale images have single intensity values per pixel (0-255).

cv.imshow('Gray', gray)
# Displays the grayscale image in a window named 'Gray'.

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# Applies simple thresholding to the grayscale image. Pixels with intensity > 150 are set to 255 (white), others to 0 (black). Returns the threshold value (150) and the thresholded image.

cv.imshow('Simple Thresholded', thresh)
# Displays the binary (black-and-white) thresholded image in a window named 'Simple Thresholded'.

# Inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# Applies inverse thresholding. Pixels with intensity > 150 are set to 0 (black), others to 255 (white). Returns the threshold value (150) and the inverse thresholded image.

cv.imshow('Simple Thresholded Inverse', thresh_inv)
# Displays the inverse binary thresholded image in a window named 'Simple Thresholded Inverse'.

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
# Applies adaptive thresholding, where the threshold value varies across the image based on local pixel neighborhoods. Uses a Gaussian-weighted average, block size 11, and subtracts 1 from the mean to fine-tune. Outputs a binary image.

cv.imshow('Adaptive thresholding', adaptive_thresh)
# Displays the adaptively thresholded binary image in a window named 'Adaptive thresholding'.

cv.waitKey(0)
# Waits indefinitely for a key press, keeping all image windows open until a key is pressed, then closes them.