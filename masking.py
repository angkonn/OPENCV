import cv2 as cv  # Import OpenCV library for image processing, alias as 'cv'. Use case: Enables image manipulation, display, and computer vision tasks.
import numpy as np  # Import NumPy for array operations, particularly for creating blank images. Use case: Create and manipulate arrays for images and masks.

img = cv.imread('Photos/cats.jpg')  # Load the image ' Cats.jpg' from the 'Photos' folder. Use case: Read an image for processing or display.
cv.imshow('Cats', img)  # Display the original image in a window titled 'Cats'. Use case: Visualize the unprocessed image for comparison.

# Create a blank grayscale image for the circle mask
blank_circle = np.zeros(img.shape[:2], dtype='uint8')  # Create a black grayscale image with the same height and width as 'img'. Use case: Serves as a canvas for drawing shapes like circles for masking.
cv.imshow('Blank Image Circle', blank_circle)  # Show the blank image for the circle mask. Use case: Visualize the starting point of the mask.

# Draw a filled white circle on the blank_circle image
mask_circle = cv.circle(blank_circle, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)  # Draw a filled white circle with radius 100, centered at (width//2 + 45, height//2). Use case: Create a circular mask to isolate a specific region of the image.
# Note: img.shape[0] is height, img.shape[1] is width; //2 computes the center, +45 shifts the circle 45 pixels right.
cv.imshow('Mask Circle', mask_circle)  # Show the circle mask. 
# Create a separate blank grayscale image for the rectangle mask
blank_rectangle = np.zeros(img.shape[:2], dtype='uint8')  # Create a new black grayscale image for the rectangle. U
# Draw a filled white rectangle on the blank_rectangle image
mask_rectangle = cv.rectangle(blank_rectangle, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)  # Draw a filled white rectangle from (width//2, height//2) to (width//2 + 100, height//2 + 100). 
cv.imshow('Mask Rectangle', mask_rectangle)  # Show the rectangle mask. 

# Mask the original image with the circle mask
masked_img_circle = cv.bitwise_and(img, img, mask=mask_circle)  # Apply the circle mask to the image, keeping only the circular region. 
cv.imshow('Masked Image Circle', masked_img_circle)  # Show the image with only the circular region visible. 

# Mask the original image with the rectangle mask
masked_img_rectangle = cv.bitwise_and(img, img, mask=mask_rectangle)  # Apply the rectangle mask to the image, keeping only the rectangular region.
cv.imshow('Masked Image Rectangle', masked_img_rectangle)  # Show the image with only the rectangular region visible. 

blank = np.zeros(img.shape[:2], dtype='uint8') 
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

weired_shape = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND',weired_shape)
weired_shape_image = cv.bitwise_and(img, img, mask= weired_shape)
cv.imshow('Weired Shape', weired_shape_image)

cv.waitKey(0)  