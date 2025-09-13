# Install required packages first:
# pip install ultralytics opencv-python requests

import cv2
from ultralytics import YOLO
import requests
import time

# WhatsApp via CallMeBot
PHONE_NUMBER = " "  # your number
API_KEY = " "               # your CallMeBot API key

def send_whatsapp_message(msg):
    try:
        url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={msg}&apikey={API_KEY}"
        requests.get(url)
        print("Notification sent!")
    except Exception as e:
        print("Error sending message:", e)

# Load YOLOv8n model (tiny, CPU-friendly)
model = YOLO("yolov8n.pt")  # downloads automatically if not present

# Initialize webcam
cap = cv2.VideoCapture(0)

last_sent_time = 0
cooldown = 30  # seconds between alerts

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO expects RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run detection
    results = model.predict(frame_rgb, verbose=False, conf=0.5)

    person_detected = False

    # Draw boxes
    for r in results:
        for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
            cls_name = model.names[int(cls)]
            if cls_name == "person":
                person_detected = True
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, cls_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    # Send WhatsApp alert
    if person_detected and time.time() - last_sent_time > cooldown:
        send_whatsapp_message("⚠️ Alert: Someone detected near your house!")
        last_sent_time = time.time()

    # Show live video
    cv2.namedWindow("Security Camera - YOLOv8", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Security Camera - YOLOv8", 1280, 720)  # width x height
    cv2.imshow("Security Camera - YOLOv8", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
