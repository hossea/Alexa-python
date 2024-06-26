import cv2
def access_camera():
    # Open the default camera (usually the webcam)
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
