import pytest

from .measurements_client import VoltageMeasurement

CLOSE_ENOUGH = 0.0001
def test_voltage_calculation(mocker):
    # mocker.patch('urequests.get')
    vm = VoltageMeasurement(full_scale_voltage=1,
        bit_count=16,
        divider_ratio=0.1,
        oid='unit_test')
    assert vm._convert_reading(65535) == pytest.approx(10, CLOSE_ENOUGH)
    assert vm._convert_reading(6553) == pytest.approx(1, CLOSE_ENOUGH)