import requests

from .exceptions import CouldNotConnectToFipeAPI


class FipeRepository:
    def __init__(self, base_url):
        """
        Initialize the RestAPIRepository with a base URL for the API.

        Args:
            base_url (str): The base URL of the REST API.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None):
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
    
    def fetch_brands(self):
        """
        Send a GET request to the "brands" endpoint.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            List[dict]: The list of brands.
        """
        return self.get('fipe/api/v1/carros/marcas')

    def fetch_cars(self, brand_id):
        """
        Send a GET request to the "modelos" endpoint.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            List[dict]: The list of cars.
        """
        response = self.get(f'fipe/api/v1/carros/marcas/{brand_id}/modelos')
        return response.json()['modelos']
