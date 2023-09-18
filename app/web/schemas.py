from typing import List

from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    api: bool
    database: bool


class Credentials(BaseModel):
    username: str
    password: str


class ImportDataResult(BaseModel):
    details: str


class Brand(BaseModel):
    code: str
    name: str


class FetchBrands(BaseModel):
    brands: List[Brand]
