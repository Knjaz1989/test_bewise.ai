from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.TEXT)
    uuid: uuid4 = sa.Column(sa.UUID, unique=True)


class Audio(Base):
    __tablename__ = 'audios'

    id: uuid4 = sa.Column(sa.UUID, primary_key=True, unique=True)
    name: str = sa.Column(sa.TEXT)
    data: bytes = sa.Column(sa.LargeBinary)
    user_id = sa.Column(
        sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE')
    )
