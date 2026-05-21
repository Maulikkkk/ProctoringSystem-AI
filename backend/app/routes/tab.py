from fastapi import APIRouter

from app.utils.session_manager import increment_event

router = APIRouter()

@router.post("/tab-switch")
def tab_switch():

    increment_event("tab_switch_count")

    return {
        "message": "Tab switch detected"
    }