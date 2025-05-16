import cv2 as cv  

img = cv.imread('Photos/cats.jpg')  
cv.imshow('Cats', img) 

# Averaging
average = cv.blur(img, (3,3))  # Apply averaging blur with a 3x3 kernel to smooth the image by averaging pixel values in the neighborhood. 
# Use case: Reduces image noise and fine details, useful for basic smoothing or preparing images for further processing.
cv.imshow('Average Blur', average) 


# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)  # Apply Gaussian blur with a 3x3 kernel and sigma=0, using a Gaussian distribution to weigh pixel values. Use case: Reduces noise while preserving edges better than averaging, commonly used in preprocessing for object detection or image enhancement.
cv.imshow('Gaussian Blur', gaussian)  

# Median Blur
median = cv.medianBlur(img, 3)  # Apply median blur with a kernel size of 3, replacing each pixel with the median value of its neighborhood. Use case: Effectively removes salt-and-pepper noise while maintaining edge sharpness, ideal for cleaning noisy images in photography or medical imaging.
cv.imshow('Median Blur', median) 

# Bilateral 
bilateral = cv.bilateralFilter(img, 10, 35, 25)  # Apply bilateral filter with diameter=10, sigmaColor=35, sigmaSpace=25 to smooth the image while preserving edges. Use case: Smooths textures while keeping edges intact, perfect for artistic effects, portrait enhancement, or preprocessing in computer vision tasks like segmentation.
cv.imshow('Bilateral Blur', bilateral)  

cv.waitKey(0) 