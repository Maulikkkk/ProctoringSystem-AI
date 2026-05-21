from fastapi import APIRouter

from app.utils.session_manager import load_session

router = APIRouter()

@router.get("/session-stats")
def get_stats():

    return load_session()