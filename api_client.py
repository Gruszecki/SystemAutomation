import logging

import requests

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, ip: str):
        self.base_url = f'http://{ip}'

    def send_request(self, endpoint: str, params: dict = None):
        url = f'{self.base_url}/{endpoint}'

        try:
            response = requests.get(url, params=params, timeout=5)
            return response
        except requests.exceptions.ConnectTimeout:
            logger.error(f'Timeout: could not connect to {url}')
