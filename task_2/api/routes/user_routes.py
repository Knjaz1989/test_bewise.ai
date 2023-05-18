from fastapi import APIRouter

from views.user_views import create_user


user_router = APIRouter(prefix='/user')


user_router.add_api_route(
    path="/create", endpoint=create_user, methods=["POST"],
)
