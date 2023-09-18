from app.repository import FipeRepository, QueueRepository, CarsRepository
from app.core.services import ImportCarsService
from app.settings import Settings


settings = Settings()

fipe_repository = FipeRepository(settings.fipe_base_url)
queue_repository = QueueRepository(
    settings.queue_host, 
    settings.queue_port, 
    settings.queue_username, 
    settings.queue_password, 
    settings.queue_name
)
cars_repository = CarsRepository(
    settings.db_connection_str, 
    settings.db_name, 
    settings.db_collection_name
)

service = ImportCarsService(fipe_repository, queue_repository, cars_repository)
service()
