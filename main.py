from fastapi import FastAPI

from api.chat_channel import get_current_message_id

app = FastAPI()

app.include_router(get_current_message_id.router)