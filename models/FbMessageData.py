from enum import Enum

from pydantic import BaseModel

from models.WebhookRequest import ID

class TextMessage(BaseModel):
    text: str

class MessagingType(str, Enum):
    RESPONSE = "RESPONSE"

class FbMessageData(BaseModel):
    recipient: ID
    messaging_type: MessagingType
    message: TextMessage
    access_token: str