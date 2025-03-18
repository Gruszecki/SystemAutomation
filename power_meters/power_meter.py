from api_client import ApiClient
from config import power_meter_ip


class PowerMeter:
    def __init__(self):
        self.api_client = ApiClient(power_meter_ip)

    def get_signal_power(self):
        return self.api_client.send_request(endpoint='get_power')
