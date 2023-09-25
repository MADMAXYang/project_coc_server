from fastapi import APIRouter, WebSocket
from plugins.ws.current_serial_number import get_chat_channels_message_serial_number
import json

router = APIRouter()


@router.websocket_route("/ws/get-current-serial-number")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_json()
        await ws.send_json(json.dumps(
                {
                    "serial_number": get_chat_channels_message_serial_number(json.load(data)),
                }
            )
        )
