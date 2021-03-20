import pytest

from .measurements_client import VoltageMeasurement

def test_voltage_calculation(mocker):
    # mocker.patch('urequests.get')
    vm = VoltageMeasurement(full_scale_voltage=1,
        bit_count=16,
        divider_ratio=0.1,
        oid='unit_test')
    assert vm._convert_reading(65535) == pytest.approx(10, 0.001)
    assert vm._convert_reading(6553) == pytest.approx(1, 0.001)