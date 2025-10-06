#import mediapipe as mp
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  # Capture frame-by-frame,ret=Boolean → True if the frame was successfully read, False otherwise
    if not ret:
        break
    cv2.imshow("Camera", frame)  # Display the video

    # Press 'q' to quit
    if cv2.waitKey(1)==27:
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()