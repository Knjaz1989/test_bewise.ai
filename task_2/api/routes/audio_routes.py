from fastapi import APIRouter

from views.audio_views import create_audio


audio_router = APIRouter(prefix='/audio')


audio_router.add_api_route(
    path="/create", endpoint=create_audio, methods=["POST"],
)
