from fastapi import Depends, Form

from database.db_sync import get_session


async def create_audio(name: str = Form(), session=Depends(get_session)):
    pass
