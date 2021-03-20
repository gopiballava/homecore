
from .measurements import Measurements


def test_measurements():
    m = Measurements()
    m.new_reading("temp", 8, 2500)
