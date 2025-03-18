from devices.base_device import BaseDevice
from config import signal_generator_ip


class SignalGenerator(BaseDevice):
    def __init__(self):
        super().__init__(ip=signal_generator_ip)

    def start(self, freq: int, power: int):
        return self.send_request(endpoint='start', params={'freq': f'{freq}m', 'power': power})

    def stop(self):
        return self.send_request(endpoint='stop')
