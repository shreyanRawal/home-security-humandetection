#  Home Security System with YOLOv8 and WhatsApp Alerts

This is a **real-time home security system** that detects people near your property using a webcam and **sends instant WhatsApp notifications** via CallMeBot.  
The system leverages **YOLOv8** for object detection, OpenCV for video processing, and Python for automation.

---

##  Features
- Real-time **person detection** using YOLOv8.  
- Sends **WhatsApp alerts** when a person is detected.  
- **Cooldown system** to avoid repeated alerts in a short time.  
- Works with a standard webcam (no extra hardware required).  
- Visual display of detected persons with bounding boxes.

---

##  Tech Stack
- **Programming Language:** Python 3.x  
- **Libraries:**  
  - [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)  
  - [OpenCV](https://opencv.org/)  
  - [Requests](https://pypi.org/project/requests/)  
- **Notification Service:** [CallMeBot WhatsApp API](https://www.callmebot.com/blog/free-api-whatsapp-messages/)  

