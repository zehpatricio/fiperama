from abc import ABC, abstractmethod
from app.repository import FipeRepository, QueueRepository


class BaseService(ABC):
    """
    Base class for services.

    Attributes:
        fipe_repository (FipeRepository): repository.
        queue_repository (QueueRepository): repository.
    """
    fipe_repository: FipeRepository
    queue_repository: QueueRepository

    def __init__(
        self, 
        fipe_repository: FipeRepository, 
        queue_repository: QueueRepository
    ) -> None:
        self.fipe_repository = fipe_repository
        self.queue_repository = queue_repository

    @abstractmethod
    def __call__(*args):
        pass
