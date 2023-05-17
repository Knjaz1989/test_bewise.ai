from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from database.models import Question


async def save_question(session: AsyncSession, data: dict):
    try:
        await session.execute(insert(Question).values(**data))
        return True
    except IntegrityError as err:
        return False
