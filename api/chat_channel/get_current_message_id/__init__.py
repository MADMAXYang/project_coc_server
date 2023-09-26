from fastapi import APIRouter
from request_body.chat_channel import request_get_current_message_id
from plugins.channel.current_serial_number import get_chat_channels_message_id


router = APIRouter()


@router.put("/chat-channel/get-current-message-id")
async def get_current_message_id(request: request_get_current_message_id):
    request_dict = request.dict()
    get_chat_channels_message_id(request_dict["channel_id"])
