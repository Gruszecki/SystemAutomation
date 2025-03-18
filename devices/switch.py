from devices.base_device import BaseDevice
from config import switch_ip


class Switch(BaseDevice):
    def __init__(self):
        super().__init__(ip=switch_ip)

    def set_input_port(self, port: int):
        return self.send_request(endpoint='input', params={'port': port})
