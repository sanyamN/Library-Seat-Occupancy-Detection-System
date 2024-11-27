import cv2
cap = cv2.VideoCapture("http://192.168.74.153:8080/video")

if not cap.isOpened():
    print("Error: Could not open video stream from camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Process the frame
    

    # Display the resulting frame
    cv2.imshow('Real-time Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
