from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_multiple_people(image):

    results = model(image)

    people = []

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            label = model.names[cls]
            confidence = float(box.conf[0])
            if label == "person" and confidence > 0.6:

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                people.append({
                    "label": "person",
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                })

    return people