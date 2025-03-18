from api_client import ApiClient
from config import signal_generator_ip
from signal_generators.base_signal_generator import BaseSignalGenerator


class SignalGeneratorA(BaseSignalGenerator):
    def __init__(self):
        self.api_client = ApiClient(ip=signal_generator_ip)

    def start(self, freq: int, power: int):
        return self.api_client.send_request(endpoint='start', params={'freq': f'{freq}m', 'power': power})

    def stop(self):
        return self.api_client.send_request(endpoint='stop')
