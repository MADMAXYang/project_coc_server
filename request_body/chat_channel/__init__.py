from pydantic import BaseModel


class request_get_current_message_id(BaseModel):
    channel_id: int
