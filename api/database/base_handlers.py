from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Question


async def save_question(session: AsyncSession, data: dict):
    insert_stm = insert(Question).values(**data)
    insert_data = await session.execute(
        insert_stm.on_conflict_do_nothing().returning(Question)
    )
    await session.commit()
    insert_data = insert_data.scalars().all()
    return insert_data
