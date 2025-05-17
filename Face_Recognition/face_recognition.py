import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Loads a pre-trained Haar Cascade model for face detection from OpenCV's data directory, used to detect faces in images.

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# Defines a list of names corresponding to people whose faces are trained for recognition (labels for face recognition).

# features = np.load('Face_Recognition/features.npy')


# labels = np.load('Face_Recognition/features.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Creates an LBPH (Local Binary Patterns Histograms) face recognizer object, used for recognizing faces based on trained data.

face_recognizer.read('face_trained.yml')
# Loads a pre-trained face recognition model from the file 'face_trained.yml', which contains trained face data.

img = cv.imread(r'C:\Users\88018\Desktop\OPENCV\Faces\val\ben_afflek\2.jpg')
# Loads a color image (of Ben Affleck) from the specified path into a NumPy array for processing.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Converts the color image to grayscale, as face detection and recognition typically work on grayscale images.

cv.imshow('Person', gray)
# Displays the grayscale image in a window named 'Person' for visualization.

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
# Detects faces in the grayscale image using the Haar Cascade model. Returns rectangles (x, y, width, height) for each detected face. Scale factor 1.1 and minNeighbors 4 control detection sensitivity.

for (x, y, w, h) in faces_rect:
# Loops through each detected face rectangle, where x, y are the top-left corner coordinates, and w, h are the width and height.

    faces_roi = gray[y:y+h, x:x+w]
    # Extracts the region of interest (ROI) of the detected face from the grayscale image (a cropped portion containing the face).

    label, confidence = face_recognizer.predict(faces_roi)
    # Predicts the identity of the face in the ROI using the trained LBPH model. Returns a label (index of the person in 'people') and a confidence score (lower is better).

    print(f'Label = {label} with a confidence of {confidence}')
    # Prints the predicted label (index) and confidence score to the console for debugging or verification.

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    # Adds the predicted person's name (from 'people' list) as text on the original color image at position (20, 20) in green color.

    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    # Draws a green rectangle around the detected face on the original color image to highlight the face.

cv.imshow('Detected face', img)


cv.waitKey(0)
