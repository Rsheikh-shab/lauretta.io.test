import cv2
import urllib.request as urllib
import numpy as np


cascadePath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# Load image from the url, the url expire in 5 second so need new new image_url
image_url = urllib.urlopen('https://hackattic.com/_/faces/4266d8f9.97ad.4ca1.8a53.0a23740d0f0f')
arr = np.asarray(bytearray(image_url.read()), dtype=np.uint8)
image = cv2.imdecode(arr, -1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces".format(len(faces)))


for face_location in faces:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite("result.jpg", image)
cv2.waitKey(0)
