import logging

import pytest

from signal_generators.signal_generator_a import SignalGeneratorA
from switches.switch_a import SwitchA
from benches.bench_a import BenchA


class TestPowerCheck:
    @pytest.mark.parametrize('freq, input_power, channel, port, target_power', [
        (10, 0, 1, 1, 20),
        (10, 5, 1, 1, 20),
        (10, 10, 1, 1, 20),
        (10, 20, 1, 1, 20),
        (10, 25, 1, 1, 20),
    ])
    def test_power_check(self, freq, input_power, channel, port, target_power):
        # threshold = 0
        # device_a = BenchA(SignalGeneratorA(), SwitchA())
        #
        # device_a.setup(freq=10, input_power=0, channel=1, port=1)
        # actual_power = device_a.get_power()
        # device_a.stop()
        actual_power = 10
        threshold = 1
        assert abs(target_power-actual_power) <= threshold, f'Actual power {actual_power} put of threshold {threshold}'
