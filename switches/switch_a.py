from api_client import ApiClient
from config import switch_ip
from switches.base_switch import BaseSwitch


class SwitchA(BaseSwitch):
    def __init__(self):
        self.api_client = ApiClient(ip=switch_ip)

    def set_input_port(self, port: int):
        return self.api_client.send_request(endpoint='input', params={'port': port})
