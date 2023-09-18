import json

from app.repository import FipeRepository, QueueRepository, CarsRepository
from .base_service import BaseService


class ImportCarsService(BaseService):
    """
    Service to fetch cars data and persist it into the database.
    """

    def __init__(
        self, 
        fipe_repository: FipeRepository, 
        queue_repository: QueueRepository,
        cars_repository: CarsRepository
    ) -> None:
        super().__init__(fipe_repository, queue_repository)
        self.cars_repository = cars_repository

    def import_cars(self, _, __, ___, brand_data):
        brand = json.loads(brand_data.decode('utf-8').replace("'", "\""))
        cars = self.fipe_repository.fetch_cars(brand["codigo"])
        for car in cars:
            self.cars_repository.insert(car)

    def __call__(self):
        self.queue_repository.consume_messages(self.import_cars)
