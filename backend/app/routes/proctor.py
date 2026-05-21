from fastapi import APIRouter, UploadFile, File

from app.utils.image_utils import bytes_to_image

from app.services.face_detection import detect_face
from app.services.person_detection import detect_multiple_people
from app.services.phone_detection import detect_phone
from app.services.gaze_tracking import detect_looking_away
from app.services.risk_engine import calculate_risk

router = APIRouter()

@router.post("/analyze-frame")
async def analyze_frame(
    file: UploadFile = File(...)
):

    contents = await file.read()

    image = bytes_to_image(contents)

    face_detected = detect_face(image)

    people_count = detect_multiple_people(image)

    phone_detected = detect_phone(image)

    looking_away = detect_looking_away(image)

    data = {
        "face_detected": face_detected,
        "multiple_people": people_count,
        "phone_detected": phone_detected,
        "looking_away": looking_away
    }

    risk_score = calculate_risk(data)

    data["risk_score"] = risk_score

    return data