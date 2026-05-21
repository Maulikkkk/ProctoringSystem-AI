# REALTIME FRAME RISK
def calculate_risk(data):

    score = 0

    if data["phone_detected"]:
        score += 40

    if data["looking_away"]:
        score += 20

    if data["multiple_people"] > 1:
        score += 40

    return min(score, 100)


# FINAL SESSION RISK
def calculate_final_risk(session_data):

    score = 0

    # PHONE
    score += (
        session_data["phone_count"] * 25
    )

    # LOOKING AWAY
    score += (
        session_data["looking_away_count"] * 5
    )

    # MULTIPLE PEOPLE
    score += (
        session_data["multiple_people_count"] * 40
    )

    # TAB SWITCH
    score += (
        session_data["tab_switch_count"] * 10
    )

    # LIMIT
    score = min(score, 100)

    # LEVEL
    if score < 30:
        level = "Low"

    elif score < 70:
        level = "Moderate"

    else:
        level = "High"

    return {
        "score": score,
        "level": level
    }