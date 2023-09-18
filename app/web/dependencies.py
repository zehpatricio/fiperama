from fastapi import Depends

from app.settings import Settings
from app.core.services import ImportBrandsService, FetchBrandsService
from app.repository import FipeRepository, QueueRepository, BrandsRepository


def make_settings() -> Settings:
    return Settings()


def make_fipe_repository(settings: Settings = Depends(make_settings)):
    return FipeRepository(settings.fipe_base_url)


def make_brands_repository(settings: Settings = Depends(make_settings)):
    return BrandsRepository(
        settings.db_connection_str, 
        settings.db_name, 
        settings.db_collection_name
    )

def make_queue_repository(settings: Settings = Depends(make_settings)):
    return QueueRepository(
        host=settings.queue_host,
        port=settings.queue_port,
        username=settings.queue_username,
        password=settings.queue_password,
        queue_name=settings.queue_name,
    )


def make_import_data_service(
    fipe_repository: FipeRepository = Depends(make_fipe_repository), 
    queue_repository: QueueRepository = Depends(make_queue_repository)
) -> ImportBrandsService:
    return ImportBrandsService(fipe_repository, queue_repository)


def make_fetch_brands_service(
    brands_repository: BrandsRepository = Depends(make_brands_repository), 
) -> FetchBrandsService:
    return FetchBrandsService(brands_repository)
