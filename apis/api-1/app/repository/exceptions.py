
class CouldNotConnectToFipeAPI(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(
            f"Could not connect to Fipe API. HTTP status code: {status_code}"
        )
