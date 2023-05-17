import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    question = sa.Column(sa.TEXT)
    answer = sa.Column(sa.TEXT)
    created_date = sa.Column(sa.TEXT)
