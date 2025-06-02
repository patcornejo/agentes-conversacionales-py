from typing import List

from pydantic import BaseModel

class ID(BaseModel):
    id: str

class Message(BaseModel):
    mid: str
    text: str

class FbMessage(BaseModel):
    sender:ID
    recipient:ID
    timestamp:int
    message: Message

class Entry(BaseModel):
    time: int
    id: str
    messaging: List[FbMessage]

class WebhookRequest(BaseModel):
    object: str
    entry: List[Entry]