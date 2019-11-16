# Copyright Gopiballava Flaherty 2018

import forecastio

HOME_LAT = 40.538276
HOME_LONG = -80.172897

# This key should not be used by other developers; it's in here for now until
# I have my key sharing system working. It's not a very sensitive key.
FORECAST_API_KEY = '513e293d89c11ed1f421a054ed49bfd4'


def get_current():
    fio = forecastio.load_forecast(FORECAST_API_KEY, HOME_LAT, HOME_LONG)
    now = fio.currently()
    return now.d

