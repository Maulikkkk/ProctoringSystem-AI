import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh()

def detect_looking_away(image):

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return False

    face_landmarks = results.multi_face_landmarks[0]

    nose = face_landmarks.landmark[1]

    nose_x = nose.x

    if nose_x < 0.35 or nose_x > 0.65:
        return True

    return False