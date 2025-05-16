import cv2 as cv  # Import OpenCV library for image processing, alias it as 'cv'
import matplotlib.pyplot as plt  # Import Matplotlib's pyplot module for displaying images

img = cv.imread('Photos/boston.png')  # Load the image 'boston.png' from the 'Photos' folder
cv.imshow('Boston', img)  # Show the original image in a window titled 'Boston'

# plt.imshow(img)  # This would display the image with Matplotlib (commented out)
# plt.show()  # This would show the Matplotlib plot (commented out)

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert the image from BGR to grayscale
cv.imshow('Gray', gray)  # Show the grayscale image in a window titled 'Gray'

# BGR to HSV format
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # Convert the image from BGR to HSV color space
cv.imshow('HSV', hsv)  # Show the HSV image in a window titled 'HSV'

# BGR to L*a*b 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)  # Convert the image from BGR to L*a*b color space
cv.imshow('LAB', lab)  # Show the L*a*b image in a window titled 'LAB'

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert the image from BGR to RGB color space
cv.imshow('RGB', rgb)  # Show the RGB image in a window titled 'RGB'

# hsv to bgr 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)  # Convert the HSV image back to BGR
cv.imshow('HSV --> BGR', hsv_bgr)  # Show the converted image in a window titled 'HSV --> BGR'

# lab to bgr 
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)  # Convert the L*a*b image back to BGR
cv.imshow('LAB --> BGR', lab_bgr)  # Show the converted image in a window titled 'LAB --> BGR'

plt.imshow(rgb)  # Display the RGB image using Matplotlib
plt.show()  # Show the Matplotlib plot

cv.waitKey(0)  # Wait for a key press to close all OpenCV windows