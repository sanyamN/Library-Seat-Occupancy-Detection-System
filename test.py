

from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import time



# Load the trained YOLOv8 model
model = YOLO("best.pt")

# Function to test the model on a single image and display counts
def predict_image(image_path):
    # Load the image
    img = Image.open(image_path)

    # Perform the prediction
    results = model.predict(img)

    # Initialize counters
    occupied_count = 0
    unoccupied_count = 0

    # Plot the image with the prediction boxes
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    ax = plt.gca()

    # Loop through the detections and add them to the plot
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Move the tensor to CPU and convert to NumPy
            conf = box.conf[0].cpu().numpy()
            label = model.names[int(box.cls[0].cpu().numpy())]

            if label == 'Occupied':
                occupied_count += 1
            elif label == 'Unoccupied':
                unoccupied_count += 1

            # Draw the box
            rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, color='red', linewidth=2)
            ax.add_patch(rect)

            # Draw the label
            plt.text(x1, y1, f'{label} {conf:.2f}', color='red', fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

    # Display the counts on the image
    plt.text(10, 30, f'Occupied: {occupied_count}', color='red', fontsize=15, bbox=dict(facecolor='white', alpha=0.5))
    plt.text(10, 60, f'Unoccupied: {unoccupied_count}', color='red', fontsize=15, bbox=dict(facecolor='white', alpha=0.5))

    plt.axis('off')
    plt.show()




import cv2
import numpy as np


# Function to process and display the frame with predictions
def process_frame(frame):
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform the prediction
    results = model.predict(rgb_frame)
    occupied_count = 0
    unoccupied_count = 0

    # Loop through the detections and add them to the frame
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Move the tensor to CPU and convert to NumPy
            conf = box.conf[0].cpu().numpy()
            label = model.names[int(box.cls[0].cpu().numpy())]

            # Draw the box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            # Draw the label
            cv2.putText(frame, f'{label} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if label == 'Occupied':
                occupied_count += 1
            elif label == 'Unoccupied':
                unoccupied_count += 1
    

    
    return frame,occupied_count,unoccupied_count

# Capture video from the laptop's camera
#cap = cv2.VideoCapture("http://192.168.74.153:8080/video")

def OpenCamera():
    cap = cv2.VideoCapture(0)
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
        processed_frame,occupied_count,unoccupied_count = process_frame(frame)

        
        # Display the resulting frame
        cv2.imshow('Real-time Object Detection', processed_frame)
        

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()
