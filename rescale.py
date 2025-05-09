import cv2 as cv

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)

def rescaleFrame(frame,scale = 0.75):
    # this wil work for images, videos and live video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

# capture image

# resized_image = rescaleFrame(img)
# cv.imshow('Cat Resized',resized_image)
# cv.waitKey(0)


# another method
def changeRes(width, height):
    # this only works for live videos
    capture.set(3,width)
    capture.set(4,height)

# # Reading video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read() # reads the video frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('video',frame)
    cv.imshow('video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

