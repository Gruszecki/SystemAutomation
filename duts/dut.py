from api_client import ApiClient
from config import dut_ip


class DUT:
    def __init__(self):
        self.api_client = ApiClient(ip=dut_ip)

    def set_output_channel(self, channel: int):
        return self.api_client.send_request(endpoint='out', params={'channel': channel})
