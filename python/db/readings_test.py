import pytest

from .readings import reading_manager

def test_new_id():
    rm = reading_manager()
    id_a = rm._create_or_get_reading_name_id('lab_power_1.voltage')
    id_b = rm._create_or_get_reading_name_id('lab_power_1.current')
    assert(id_a != id_b)