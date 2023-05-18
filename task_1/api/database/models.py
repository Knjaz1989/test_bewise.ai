import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id: int = sa.Column(sa.Integer, primary_key=True, unique=True)
    question: str = sa.Column(sa.TEXT)
    answer: str = sa.Column(sa.TEXT)
    created_date: str = sa.Column(sa.TEXT)
