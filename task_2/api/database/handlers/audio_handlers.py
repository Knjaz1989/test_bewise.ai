from uuid import uuid4

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def add_user(session: AsyncSession, name: str):
    insert_stm = insert(User).values(
        name=name, uuid=uuid4()
    )
    insert_data = await session.execute(
        insert_stm.returning(User.id, User.uuid)
    )
    await session.commit()
    insert_data = insert_data.mappings().one()
    return insert_data