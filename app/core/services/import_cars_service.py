import json

from app.core.models import Brand
from app.repository import FipeRepository, QueueRepository, BrandsRepository
from .base_service import BaseService


class ImportCarsService(BaseService):
    """
    Service to fetch cars data and persist it into the database.
    """

    def __init__(
        self, 
        fipe_repository: FipeRepository, 
        queue_repository: QueueRepository,
        brands_repository: BrandsRepository
    ) -> None:
        super().__init__(fipe_repository, queue_repository)
        self.brands_repository = brands_repository

    def import_cars(self, _, __, ___, brand_data):
        print(f'[+] Received {brand_data}')
        
        brand_dict = json.loads(brand_data.decode('utf-8').replace("'", "\""))
        brand = Brand(**brand_dict)
        
        cars = self.fipe_repository.fetch_cars(brand.code)
        brand.cars = cars
        
        self.brands_repository.insert(brand)

    def __call__(self):
        self.queue_repository.consume_messages(self.import_cars)
