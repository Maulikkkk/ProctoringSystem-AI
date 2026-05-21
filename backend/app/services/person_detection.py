from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_multiple_people(image):

    results = model(image)

    person_count = 0

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            if label == "person":
                person_count += 1

    return person_count