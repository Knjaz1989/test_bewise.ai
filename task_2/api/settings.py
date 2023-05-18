from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Config(BaseSettings):
    DEBUG_SERVER: bool = False

    SYNC_SQLALCHEMY_URL: str
    ASYNC_SQLALCHEMY_URL: str


config = Config()
