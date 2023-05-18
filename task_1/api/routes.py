from fastapi import APIRouter, status

from views import get_questions


api_router = APIRouter()


api_router.add_api_route(
    path="/", endpoint=get_questions, methods=["POST"],
)
