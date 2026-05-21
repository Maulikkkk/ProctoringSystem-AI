from fastapi import APIRouter, UploadFile, File

from app.utils.image_utils import bytes_to_image

from app.services.face_detection import detect_face
from app.services.person_detection import detect_multiple_people
from app.services.phone_detection import detect_phone
from app.services.gaze_tracking import detect_looking_away
from app.services.risk_engine import calculate_risk

from app.utils.session_manager import increment_event

router = APIRouter()

# -------------------------
# EVENT MEMORY
# -------------------------
last_states = {
    "looking_away": False,
    "phone": False,
    "multiple_people": False
}

@router.post("/analyze-frame")
async def analyze_frame(
    file: UploadFile = File(...)
):

    global last_states

    contents = await file.read()

    image = bytes_to_image(contents)

    # FACE
    face_detected = detect_face(image)

    # PEOPLE
    people = detect_multiple_people(image)

    people_count = len(people)

    # PHONE
    phones = detect_phone(image)

    phone_detected = len(phones) > 0

    # GAZE
    looking_away = detect_looking_away(image)

    # RESPONSE
    data = {
        "face_detected": face_detected,
        "multiple_people": people_count,
        "phone_detected": phone_detected,
        "looking_away": looking_away,
        "risk_score": 0,
        "detections": [
            *people,
            *phones
        ]
    }

    # RISK SCORE
    risk_score = calculate_risk(data)

    data["risk_score"] = risk_score

    # -------------------------
    # SMART EVENT TRACKING
    # -------------------------

    # PHONE
    if (
        phone_detected
        and not last_states["phone"]
    ):
        increment_event("phone_count")

    # LOOKING AWAY
    if (
        looking_away
        and not last_states["looking_away"]
    ):
        increment_event("looking_away_count")

    # MULTIPLE PEOPLE
    if (
        people_count > 1
        and not last_states["multiple_people"]
    ):
        increment_event("multiple_people_count")

    # -------------------------
    # UPDATE MEMORY
    # -------------------------

    last_states["phone"] = phone_detected

    last_states["looking_away"] = looking_away

    last_states["multiple_people"] = (
        people_count > 1
    )

    return data