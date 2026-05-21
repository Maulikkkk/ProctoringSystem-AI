import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection

face_detector = mp_face.FaceDetection(
    min_detection_confidence=0.5
)

def detect_face(image):

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = face_detector.process(rgb)

    if results.detections:
        return True

    return False