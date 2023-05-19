from fastapi import APIRouter

from views.audio_views import create_audio, get_audio


audio_router = APIRouter(prefix='/record')


audio_router.add_api_route(
    path="/", endpoint=create_audio, methods=["POST"],
)
audio_router.add_api_route(
    path="/", endpoint=get_audio, methods=["GET"],
)
