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
    
    def get_marcas(self):
        """
        Send a GET request to the "marcas" endpoint.

        Raises:
            CouldNotConnectToFipeAPI: if there is any error in the connection 
                with FipeAPI.

        Returns:
            List[dict]: The list of marcas.
        """
        return self.get('fipe/api/v1/carros/marcas')
