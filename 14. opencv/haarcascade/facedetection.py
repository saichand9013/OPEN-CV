import numpy as np
import cv2

# Load the Haar Cascade for face detection
face_classifier = cv2.CascadeClassifier(r"C:\Users\Sai\A in Acodes\data science\14. opencv\haarcascade\haarcascade_frontalface_default.xml")

image = cv2.imread(r"C:\Users\Sai\A in Acodes\data science\14. opencv\haarcascade\selfie.jpg")

#image = cv2.imread(r"C:\Users\Admin\3IMAX_SOFTWARE_TECH\Desktop\WORK\2_DATASCIENCE PROJECT\10_Computer vi...

# Check if the image is loaded correctly
if image is None:
    print("Error: image not found or cannot be loaded!")
    exit()  # exit if image is not loaded

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Check if faces are detected
if len(faces) == 0:
    print("No faces found!")
else:
    # Draw rectangles around the faces
    for (x, y, w, h) in faces: # (x, y) is the top-left corner, and (w, h) is the width and height of
        cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)

# Display the output image
cv2.imshow('face Detection', image)
cv2.waitKey(0) # a wait for a key press to close the window

# Close all OpenCV windows
cv2.destroyAllWindows()