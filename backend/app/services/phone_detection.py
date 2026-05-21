from ultralytics import YOLO

model = YOLO("yolov8s.pt")

phone_memory = 0

def detect_phone(image):

    global phone_memory

    results = model(image)

    detections = []

    phone_found = False

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            confidence = float(box.conf[0])

            if (
                label == "cell phone"
                and confidence > 0.35
            ):

                phone_found = True

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                detections.append({
                    "label": "phone",
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                })

    # INSTANT DETECTION
    if phone_found:

        phone_memory = 3

        return detections

    # SMOOTH EXIT
    else:

        if phone_memory > 0:

            phone_memory -= 1

            return detections

    return []