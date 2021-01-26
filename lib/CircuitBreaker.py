from robot.api.deco import keyword
ROBOT_AUTO_KEYWORDS = False
from amst_db import get_communicating_meter_cbconnected_localdisconnect_enabled


@keyword
def select_meter(cbstatus, commstatus):
    (meterpoint, meter) = get_communicating_meter_cbconnected_localdisconnect_enabled()
    print(cbstatus)
    print(commstatus)
    print(meter)
    print(meterpoint)
    return (meterpoint, meter)


@keyword
def ensure_cb(mp_meter):
    print("ensure> ")
    print(mp_meter)
    return "user"
