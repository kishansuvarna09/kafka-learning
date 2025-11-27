from pydantic import BaseModel

class Event(BaseModel):
    user_id: int
    action: str
    timestamp: str