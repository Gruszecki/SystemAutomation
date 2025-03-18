from tests.test_base import TestBase


class TestPowerCheck(TestBase):
    def test_power_check_channel_1_input_0_freq_10_target_20(self):
        assert self.power_check(freq=10, input_power=0, channel=1, target=20)

    def test_power_check_channel_1_input_5_freq_10_target_20(self):
        assert self.power_check(freq=10, input_power=5, channel=1, target=20)
