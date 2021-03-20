# import urequests

from .measurements import SERVER_PORT

# Why is this here? Lazyness.
SERVER_IP = '192.168.87.2'


class MeasurementsClient:
    def __init__(self):
        pass
    
    def _send_reading(self, reading_type, oid, value):
        # response = urequests.get('http://{}:{}/new_reading/{}/{}/{}'.format(SERVER_IP, SERVER_PORT, reading_type, oid, value))
        # if response.status_code != 200:
        #    print('http error code {}, reason {}'.format(response.status_code, response.reason))


class VoltageMeasurement(MeasurementClient):
    def __init__(self, full_scale_voltage=None, bit_count=None, divider_ratio=None, oid=None):
        self._full_scale_voltage = full_scale_voltage
        self._bit_count = bit_count
        self._full_scale = 2 ** self._bit_count
        self._divider_ratio = divider_ratio
        self._oid = oid
    
    def _convert_reading(self, ADC_value):
        adc_fraction = ADC_value / self._full_scale
        raw_voltage = self._full_scale_voltage * adc_fraction
        return raw_voltage * self._divider_ratio
    
    def send_reading(self, ADC_value):
        self._send_reading('voltage', self._oid, self._convert_reading(ADC_value))
        