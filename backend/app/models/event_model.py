from pydantic import BaseModel
from datetime import datetime

class EventModel(BaseModel):
    timestamp: datetime
    event_type: str
    details: dict
