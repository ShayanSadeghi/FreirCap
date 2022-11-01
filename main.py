import numpy as np
import cv2 as cv

img = cv.imread("/home/shayan/Pictures/faces/pexels-photo-3184419.jpeg")

# cv.imshow("gray",gray)

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")


def face_detect(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 1)

    for (x, y, w, h) in faces:
        # cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = frame[y:y + int(1.5 * h), x:x + int(1.5 * w)]
        blurred_face = cv.GaussianBlur(roi, (23, 23), 30)
        frame[y:y + int(1.5 * h), x:x + int(1.5 * w)] = blurred_face
    return frame


blurred_img = face_detect(img)
cv.imshow("blurred", blurred_img)

cv.imshow("face", img)

cv.waitKey(0)