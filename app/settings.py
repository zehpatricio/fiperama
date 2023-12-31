from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fiperama"
    secret_key: str
    algorithm: str

    queue_host: str
    queue_port: str
    queue_username: str
    queue_password: str
    queue_name: str

    db_connection_str: str
    db_name: str
    db_collection_name: str

    fipe_base_url: str

    class Config:
        env_file = ".env"
        extra = "allow"
