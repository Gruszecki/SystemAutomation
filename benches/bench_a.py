from duts.dut import DUT
from power_meters.power_meter import PowerMeter
from signal_generators.base_signal_generator import BaseSignalGenerator
from switches.base_switch import BaseSwitch


class BenchA:
    def __init__(self, signal_generator, switch):
        self._signal_generator: BaseSignalGenerator = signal_generator
        self._dut = DUT()
        self._switch: BaseSwitch = switch
        self._power_meter = PowerMeter()

    def setup(self, freq: int, input_power: int, channel: int, port: int):
        self._signal_generator.start(freq=freq, power=input_power)
        self._dut.set_output_channel(channel=channel)
        self._switch.set_input_port(port=port)

    def stop(self):
        self._signal_generator.stop()

    def get_power(self):
        return self._power_meter.get_signal_power()
