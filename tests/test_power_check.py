import logging

import pytest

from signal_generators.signal_generator_a import SignalGeneratorA
from switches.switch_a import SwitchA
from benches.bench_a import BenchA

logger = logging.getLogger(__name__)


class TestPowerCheck:
    @pytest.mark.parametrize('freq, input_power, channel, port, target_power', [
        (10, 0, 1, 1, 20),
        (10, 5, 1, 1, 20),
        (10, 10, 1, 1, 20),
        (10, 20, 1, 1, 20),
        (10, 25, 1, 1, 20),
    ])
    def test_power_check(self, freq, input_power, channel, port, target_power):
        logger.info(f'Running power check test with freq={freq}, input_power={input_power}, channel={channel}, '
                    f'port={port}, target_power={target_power}')

        threshold = 0
        bench_a = BenchA(SignalGeneratorA(), SwitchA())

        bench_a.setup(freq=10, input_power=0, channel=1, port=1)
        actual_power = bench_a.get_power()
        bench_a.stop()

        if actual_power is not None:
            assert abs(target_power-actual_power) <= threshold, f'Actual power {actual_power} not in expected range {target_power-threshold}-{target_power+threshold}'
        else:
            assert False, 'Could not perform test: Bench Error'
