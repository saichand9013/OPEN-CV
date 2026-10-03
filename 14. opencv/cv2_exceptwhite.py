import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green color
    low = np.array([0, 0, 0])  # lowest hue would be - 161,155,84 ( how do i found this i tested before
    high= np.array([179, 255, 255])
    #mask = cv2.inRange(hsv_frame, low_green, high_green)

    mask = cv2.inRange(hsv_frame, low, high)  #we create maskk on hsv frame and then low green or hi
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    #cv2.imshow('Red mask', mask)
    cv2.imshow('Result', result)

    key = cv2.waitKey(1)
    if key == 27:
        break