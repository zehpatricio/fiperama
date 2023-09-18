import time

import pika

from app.repository import FipeRepository, QueueRepository, BrandsRepository
from app.core.services import ImportCarsService
from app.settings import Settings


if __name__ == '__main__':
    seconds = 10
    settings = Settings()
    
    while True:
        try:
            queue_repository = QueueRepository(
                settings.queue_host, 
                settings.queue_port, 
                settings.queue_username, 
                settings.queue_password, 
                settings.queue_name
            )
            break
        except pika.exceptions.AMQPConnectionError:
            print(f'Waiting {seconds} for Rabbit')
            time.sleep(seconds)
    
    fipe_repository = FipeRepository(settings.fipe_base_url)
    cars_repository = BrandsRepository(
        settings.db_connection_str, 
        settings.db_name, 
        settings.db_collection_name
    )

    service = ImportCarsService(
        fipe_repository, 
        queue_repository, 
        cars_repository
    )
    service()
    