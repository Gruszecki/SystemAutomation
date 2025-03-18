import requests


class BaseDevice:
    def __init__(self, ip: str):
        self.base_url = f'http://{ip}'

    def send_request(self, endpoint: str, params: dict = None):
        url = f'{self.base_url}/{endpoint}'
        try:
            return requests.get(url, params=params, timeout=5)
        except requests.RequestException as e:
            print(f"Error communicating with {url}: {e}")
            return None

