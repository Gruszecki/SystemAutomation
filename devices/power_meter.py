from devices.base_device import BaseDevice
from config import power_meter_ip


class PowerMeter(BaseDevice):
    def __init__(self):
        super().__init__(ip=power_meter_ip)

    def get_signal_power(self):
        return self.send_request(endpoint='get_power')
