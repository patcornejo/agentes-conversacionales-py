import os

from typing import Annotated

from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Query

from fb import send_text_message
from llm import get_answer
from models.WebhookRequest import WebhookRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/webhook")
async def webhook(
        hub_mode: Annotated[str, Query(alias="hub.mode")],
        hub_verify_token: Annotated[str, Query(alias="hub.verify_token")],
        hub_challenge: Annotated[str, Query(alias="hub.challenge")],
):
    print(f"{hub_mode}: {hub_verify_token}: {hub_challenge}")
    verify_token = os.environ['VERIFY_TOKEN']
    if verify_token == hub_verify_token and hub_mode == 'subscribe':
        return Response(hub_challenge, status_code=200)
    return HTTPException(status_code=404, detail='Not authorized')

@app.post('/webhook')
async def fb_message(req: WebhookRequest):
    try:
        msg = req.entry[0].messaging[0].message.text
        answer = get_answer(msg)
        send_text_message(
            req.entry[0].messaging[0].recipient.id,
            req.entry[0].messaging[0].sender.id,
            answer
        )
        return Response("ok", status_code=200)
    except Exception as e:
        print(e)
    return HTTPException(status_code=404, detail='Not found')