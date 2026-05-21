from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_phone(image):

    results = model(image)

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            if label == "cell phone":
                return True

    return False