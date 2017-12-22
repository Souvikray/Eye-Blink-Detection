import numpy as np
import cv2
import dlib

JAWLINE_POINTS = list(range(0, 17))
RIGHT_EYEBROW_POINTS = list(range(17, 22))
LEFT_EYEBROW_POINTS = list(range(22, 27))
NOSE_POINTS = list(range(27, 36))
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))
MOUTH_OUTLINE_POINTS = list(range(48, 61))
MOUTH_INNER_POINTS = list(range(61, 68))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

img = cv2.imread("mypic1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.05, 12)
print("Faces", faces)
for face in faces:
    # the detected face is represented in the form of a rectangle
    x, y, w, h = face
    # draw a rectangle on the face in the image
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # convert the OpenCV rectange coordinates to Dlib rectangle
    dlib_rect = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))
    # get the facial landmarks and convert it to numpy matrix
    landmarks = np.matrix([[p.x, p.y] for p in predictor(img, dlib_rect).parts()])
    # get specific landmarks
    landmarks_display = landmarks[RIGHT_EYE_POINTS + LEFT_EYE_POINTS]
    for idx, point in enumerate(landmarks_display):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(img, str(idx), pos, cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 255))
        cv2.circle(img, pos, 2, (0, 255, 255), -1) # (image, coordinates, radius, color, thickness)

cv2.imshow("Landmarks found", img)
cv2.waitKey(0)



