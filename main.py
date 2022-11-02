from pickle import TRUE
import numpy as np
import cv2 as cv


face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")


def face_blur(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 1)

    for (x, y, w, h) in faces:
        
        if y + int(1.5 * h) < frame.shape[0]:
            h = int(1.5 * h)

        if x + int(1.5 * w) < frame.shape[1]:
            w = int(1.5 * w)

        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = frame[y : y + h, x : x + w]
        blurred_face = cv.GaussianBlur(roi, (23, 23), 25)
        frame[y : y + h, x : x + w] = blurred_face
    return frame


capture = cv.VideoCapture(0)

while True:
    ret,frame = capture.read()
    frame = face_blur(frame)
    cv.imshow("Video",frame)

    if cv.waitKey(1) == ord('q'):
        break

# blurred_img = face_blur(img)
# cv.imshow("blurred", blurred_img)
# cv.waitKey(0)
