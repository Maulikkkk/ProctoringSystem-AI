import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True
)

LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

LEFT_EYE_LEFT = 33
LEFT_EYE_RIGHT = 133

RIGHT_EYE_LEFT = 362
RIGHT_EYE_RIGHT = 263

def iris_position(iris_center, right_point, left_point):

    center_to_right = np.linalg.norm(
        iris_center - right_point
    )

    total_distance = np.linalg.norm(
        left_point - right_point
    )

    ratio = center_to_right / total_distance

    return ratio

def detect_looking_away(image):

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return False

    mesh_points = np.array([
        np.multiply(
            [p.x, p.y],
            [image.shape[1], image.shape[0]]
        ).astype(int)

        for p in results.multi_face_landmarks[0].landmark
    ])

    # LEFT EYE
    left_iris = mesh_points[LEFT_IRIS]
    left_center = np.mean(
        left_iris,
        axis=0
    ).astype(int)

    left_eye_left = mesh_points[LEFT_EYE_LEFT]
    left_eye_right = mesh_points[LEFT_EYE_RIGHT]

    left_ratio = iris_position(
        left_center,
        left_eye_right,
        left_eye_left
    )

    # RIGHT EYE
    right_iris = mesh_points[RIGHT_IRIS]
    right_center = np.mean(
        right_iris,
        axis=0
    ).astype(int)

    right_eye_left = mesh_points[RIGHT_EYE_LEFT]
    right_eye_right = mesh_points[RIGHT_EYE_RIGHT]

    right_ratio = iris_position(
        right_center,
        right_eye_right,
        right_eye_left
    )

    avg_ratio = (
        left_ratio + right_ratio
    ) / 2

    # Looking sideways
    if avg_ratio <= 0.35 or avg_ratio >= 0.65:
        return True

    return False