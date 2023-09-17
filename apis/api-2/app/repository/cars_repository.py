import pymongo

from app.core.models import Car


class CarsRepository:
    def __init__(self, connection_string, database_name, collection_name):
        """
        Initialize the CarsRepository with a connection string, database name, and collection name.

        Args:
            connection_string (str): The MongoDB connection string.
            database_name (str): The name of the MongoDB database.
            collection_name (str): The name of the MongoDB collection.
        """
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert(self, data):
        """
        Insert a car into the MongoDB collection.

        Args:
            data (dict): The car data to insert.

        Returns:
            Car: A Car instance representing the inserted car.
        """
        result = self.collection.insert_one(data)
        return Car(
            code=result["code"], 
            model=result["model"],
            notes=result["notes"],
            brand=result["brand"]
        )

    def update(self, filter_query, update_data):
        """
        Update cars in the MongoDB collection that match the filter query.

        Args:
            filter_query (dict): The query to filter cars for update.
            update_data (dict): The update data to apply to matching cars.

        Returns:
            int: The number of cars updated.
        """
        result = self.collection.update_many(filter_query, update_data)
        return result.modified_count

    def find(self, filter_query):
        """
        Find cars in the MongoDB collection that match the filter query.

        Args:
            filter_query (dict): The query to filter cars.

        Returns:
            list[Car]: A list of Car instances parsed from the matching cars.
        """
        cursor = self.collection.find(filter_query)
        result = []

        for document in cursor:
            car_instance = Car(
                code=document["code"],
                model=document["model"],
                notes=document["notes"],
                brand=document["brand"]
            )
            result.append(car_instance)

        return result
