import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    question = sa.Column(sa.TEXT)
    answer = sa.Column(sa.TEXT)
    create_date = sa.Column(sa.DateTime)
