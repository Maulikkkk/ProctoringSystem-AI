def calculate_risk(data):

    risk = 0

    if not data["face_detected"]:
        risk += 50

    if data["multiple_people"] > 1:
        risk += 70

    if data["phone_detected"]:
        risk += 40

    if data["looking_away"]:
        risk += 20

    return risk