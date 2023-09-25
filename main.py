from fastapi import FastAPI

from api.ws import get_current_serial_number

app = FastAPI()

app.include_router(get_current_serial_number.router)