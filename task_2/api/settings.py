from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Config(BaseSettings):
    DEBUG_SERVER: bool = False

    api_host: str
    api_port: int

    SYNC_SQLALCHEMY_URL: str
    ASYNC_SQLALCHEMY_URL: str


config = Config()
