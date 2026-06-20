from time import time


from ultralytics import YOLO
import cv2


# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(1)


prev_time = time()
while True:
    success, frame = cap.read()
    current_time = time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    success, frame = cap.read()

    if not success:
        print("Could not access camera")
        break

    # Detect objects
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()