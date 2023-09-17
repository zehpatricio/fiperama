from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    api: bool
    database: bool


class Credentials(BaseModel):
    username: str
    password: str


class ImportDataResult(BaseModel):
    details: str
