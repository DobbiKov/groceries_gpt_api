from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BEARER_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()

