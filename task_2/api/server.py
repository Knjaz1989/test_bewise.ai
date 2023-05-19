from fastapi import FastAPI

from routes.user_routes import user_router
from routes.audio_routes import audio_router


app = FastAPI()

app.include_router(user_router)
app.include_router(audio_router)
