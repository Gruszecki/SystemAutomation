import requests


class ApiClient:
    def __init__(self, ip: str):
        self.base_url = f'http://{ip}'

    def send_request(self, endpoint: str, params: dict = None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, params=params, timeout=5)

        # TODO: logging

        return response
