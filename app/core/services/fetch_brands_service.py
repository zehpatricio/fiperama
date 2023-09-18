from dataclasses import asdict

from app.repository import BrandsRepository

from .base_service import BaseService


class FetchBrandsService(BaseService):
    """
    Service to fetch brands.
    """
    def __init__(self, brands_repository: BrandsRepository) -> None:
        self.brands_repository = brands_repository

    def __call__(self):
        brands = self.brands_repository.find(
            {}, include_fields=['code', 'name']
        )
        return brands
