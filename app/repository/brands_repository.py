from typing import Union, List
from dataclasses import asdict

import pymongo

from app.core.models import Brand, Car


class BrandsRepository:
    def __init__(
        self, 
        connection_string: str,
        database_name: str, 
        collection_name: str
    ):
        """
        Initialize the BrandsRepository with a connection string, d
        atabase name, and collection name.

        Args:
            connection_string (str): The MongoDB connection string.
            database_name (str): The name of the MongoDB database.
            collection_name (str): The name of the MongoDB collection.
        """
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert(self, brand: Brand) -> None:
        """
        Insert a brand into the MongoDB collection.

        Args:
            data (dict): The car data to insert.
        """
        self.collection.insert_one(asdict(brand))

    def update(self, filter_query: dict, update_data: dict) -> int:
        """
        Update brands in the MongoDB collection that match the filter query.

        Args:
            filter_query (dict): The query to filter brands for update.
            update_data (dict): The update data to apply to matching brands.

        Returns:
            int: The number of brands updated.
        """
        result = self.collection.update_many(filter_query, update_data)
        return result.modified_count

    def find(
        self, 
        filter_query: dict, 
        include_fields: list[str] = None
    ) -> Union[List[Brand], dict]:
        """
        Find brands in the MongoDB collection that match the filter query.

        Args:
            filter_query (dict): The query to filter brands.
            include_fields (list[dict]): The fields to include in the result. 
                If not provided all fields will be included.

        Returns:
            Union(list[Brand], dict): A list of Brand instances or a dict with 
                the `include_fields` fields.
        """
        cursor = self.collection.find(filter_query, projection=include_fields)
        result = []

        for brand in cursor:
            if not include_fields:
                cars = [Car(**car) for car in brand.pop('cars')]
                brand_instance = Brand(**brand, cars=cars)
                result.append(brand_instance)
            else:
                result.append(brand)

        return result
