import requests
import time
from robot.api.deco import keyword
from config import Config


@keyword
def ping_meter(meter):
    url_base = Config.ACE_API_BASE
    headers = {}
    headers['X-Thor-Apikey'] = Config.THOR_API_KEY
    headers['Content-type'] = 'application/json'
    metering_point_id = 'MP_8000100000000021'
    print("posting.....")
    data = """
    {
    "count":20
    }
    """
    url = 'http://www.vg.no'
    url = f"https://{url_base}/api/v1/MeteringPoints/{metering_point_id}/ping"
    print(url)
    start_time = time.time()
    response = requests.post(url, data=data, headers=headers)
    # response = requests.get(url)
    end_time = time.time()
    print(response)
    if end_time - start_time > 0.5:
        # raise AssertionError(f"SLa not met: elapsed {end_time - start_time} > 0.5")
        print(f"SLa not met: elapsed {end_time - start_time} > 0.5")



if __name__ == '__main__':
    ping_meter('12356')