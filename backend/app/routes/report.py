from fastapi import APIRouter

from app.services.llm_report import generate_report

router = APIRouter()

@router.get("/generate-report")
def report():

    events = [
        "Phone detected twice",
        "Candidate looked away 14 times",
        "Multiple faces detected once"
    ]

    result = generate_report(events)

    return {
        "report": result
    }