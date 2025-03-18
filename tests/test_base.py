import pytest

from devices.dut import DUT
from devices.power_meter import PowerMeter
from devices.signal_generator import SignalGenerator
from devices.switch import Switch


class TestBase:
    def power_check(self, freq: int, input_power: int, channel: int, target: int, threshold: int = 0):
        signal_generator = SignalGenerator()
        dut = DUT()
        switch = Switch()
        power_meter = PowerMeter()

        signal_generator.start(freq=freq, power=input_power)
        dut.set_output_channel(channel=channel)
        switch.set_input_port(port=channel)

        current_power = power_meter.get_signal_power()

        signal_generator.stop()

        if not current_power:
            return False

        return target - threshold <= current_power <= target + threshold
