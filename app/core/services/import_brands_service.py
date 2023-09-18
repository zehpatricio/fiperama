from dataclasses import asdict

from .base_service import BaseService


class ImportBrandsService(BaseService):
    """
    Service to fetch data and send it to the queue.
    """
    def __call__(self):
        brands = self.fipe_repository.fetch_brands()

        for brand in brands:
            self.queue_repository.publish_message(str(asdict(brand)))

        print(f"Published {len(brands)} items to the queue.")
