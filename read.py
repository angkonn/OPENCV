import cv2 as cv

# reading images
img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat',img)

# Reading video
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read() # reads the video frame by frame
#     cv.imshow('video',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


