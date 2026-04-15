"""Application configuration."""

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Multi-Agent RPG V1"
    api_prefix: str = ""
    database_url: str = "sqlite:///./game.db"
    debug: bool = True


settings = Settings()
