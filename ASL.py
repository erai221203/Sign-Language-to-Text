import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"F:\objDet\best.pt")  # Path to your best.pt

# Open the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Real-time detection loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLO detection on the current frame
    results = model.predict(source=frame, conf=0.7)  # Run detection

    # Extract the annotated image from results
    annotated_frame = results[0].plot()  # Get the frame with detections drawn on it

    # Display the annotated frame
    cv2.imshow("YOLO Live Detection", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
