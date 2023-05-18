from fastapi import Depends, Form

from database.base_handlers import add_user
from database.db_sync import get_session


async def create_user(name: str = Form(), session=Depends(get_session)):
    user_data = await add_user(session, name)
    return user_data
