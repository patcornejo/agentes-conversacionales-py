import os

import requests

from models.FbMessageData import FbMessageData, MessagingType, TextMessage
from models.FbMessageResponse import FbMessageResponse
from models.WebhookRequest import ID

FB_BASE_URL = "https://graph.facebook.com/v23.0"

s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})

def send_text_message(fr: str, to: str, text: str) -> FbMessageResponse:
    try:
        data = FbMessageData(
            recipient=ID(id=to),
            messaging_type=MessagingType.RESPONSE,
            message=TextMessage(text=text),
            access_token=os.environ["FB_ACCESS_TOKEN"],
        )
        response = s.post(f"{FB_BASE_URL}/{fr}/messages", data=data.model_dump_json())
        return FbMessageResponse(**response.json())
    except Exception as e:
        raise Exception(f"Failed to send from: {fr} to: {to} text message {text}: {e}")