from fastapi import APIRouter

from app.services.llm_report import generate_report

from app.utils.session_manager import load_session
from app.services.risk_engine import calculate_final_risk

router = APIRouter()

@router.get("/generate-report")
def report():

    session_data = load_session()

    risk = calculate_final_risk(
        session_data
    )

    result = generate_report({
        "session": session_data,
        "risk": risk
    })

    return {
        "session_data": session_data,
        "risk": risk,
        "report": result
    }