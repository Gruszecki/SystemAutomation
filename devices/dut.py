from devices.base_device import BaseDevice
from config import dut_ip


class DUT(BaseDevice):
    def __init__(self):
        super().__init__(ip=dut_ip)

    def set_output_channel(self, channel: int):
        return self.send_request(endpoint='out', params={'channel': channel})
