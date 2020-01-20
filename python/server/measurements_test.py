
from .measurements import Measurements


def test_measurements():
    m = Measurements()
    m.reading("temp", 8, 2500)
