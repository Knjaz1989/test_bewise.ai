from uuid import uuid4

from pydantic.types import UUID
from sqlalchemy import select, insert, and_
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Audio


async def add_audio(
        session: AsyncSession,
        name: str,
        data: bytes,
        user_id: int
):
    insert_stm = insert(Audio).values(
        id=uuid4(), name=name, data=data, user_id=user_id
    ).returning(Audio.id)
    query = await session.execute(insert_stm)
    audio_id = query.mappings().one()
    await session.commit()
    return audio_id


async def select_audio(session: AsyncSession, user_id: int, audio_id: UUID):
    select_stm = select(Audio).where(
        and_(user_id == Audio.user_id, audio_id == Audio.id)
    )
    query = await session.execute(select_stm)
    audio = query.scalars().one()
    return audio
