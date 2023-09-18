import requests
from typing import List

from app.core.models import Brand, Car
from .exceptions import CouldNotConnectToFipeAPI


class FipeRepository:
    def __init__(self, base_url):
        """
        Initialize the RestAPIRepository with a base URL for the API.

        Args:
            base_url (str): The base URL of the REST API.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None) -> dict:
        """
        Send a GET request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            params (dict, optional): Query parameters to include in the request.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            dict: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            # TODO: log exception tracetrack
            raise CouldNotConnectToFipeAPI(response.status_code)
    
    def fetch_brands(self) -> List[Brand]:
        """
        Send a GET request to the "brands" endpoint.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            List[dict]: The list of brands.
        """
        brands_json = self.get('fipe/api/v1/carros/marcas')
        brands = [
            Brand(code=brand['codigo'], name=brand['nome'], cars=[]) 
            for brand in brands_json
        ]
        return brands

    def fetch_cars(self, brand_id) -> List[Brand]:
        """
        Send a GET request to the "modelos" endpoint.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            List[dict]: The list of cars.
        """
        cars_json = self.get(f'fipe/api/v1/carros/marcas/{brand_id}/modelos')
        cars = [
            Car(code=car['codigo'], model=car['nome'])
            for car in cars_json['modelos']
        ]
        return cars
