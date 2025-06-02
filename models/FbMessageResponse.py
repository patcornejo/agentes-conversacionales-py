from pydantic import BaseModel


class FbMessageResponse(BaseModel):
    recipient_id: str
    message_id: str