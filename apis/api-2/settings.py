from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API-2"

    db_connection_str: str
    fipe_base_url: str

    class Config:
        env_file = ".env"
