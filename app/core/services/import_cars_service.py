from .base_service import BaseService


class ImportCarsService(BaseService):
    """
    Service to fetch data and send it to the queue.
    """
    def __call__(self):
        data = self.fipe_repository.get_brands()

        for item in data:
            self.queue_repository.publish_message(str(item))

        print(f"Published {len(data)} items to the queue.")
