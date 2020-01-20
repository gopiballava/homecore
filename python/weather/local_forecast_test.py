from .local_forecast import get_current

import pprint


def test_local_forecast():
    pprint.pprint(get_current())
