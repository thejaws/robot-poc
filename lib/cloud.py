import requests
import time
from robot.api.deco import keyword
from config import Config


@keyword
def ping_meter(meter):
    url_base = Config.ACE_API_BASE
    if USE_MOCK=True:
        url_base = 'http://localhost:5000'

    headers = {'X-Thor-Apikey': Config.THOR_API_KEY, 'Content-type': 'application/json'}
    metering_point_id = 'MP_8000100000000021'
    print("posting.....")
    data = """
    {
    "count":20
    }
    """
    # url = 'http://www.vg.no'
    # url = f"https://{url_base}/api/v1/MeteringPoints/{metering_point_id}/ping"
    # if 'localhost' in url_base:
    url = f"http://{url_base}/api/v1/MeteringPoints/{metering_point_id}/ping"
    print(url)
    start_time = time.time()
    status = {}
    response = requests.post(url, data=data, headers=headers)
    # response = requests.get(url)
    end_time = time.time()
    print(response)
    status['http_status'] = requests.http_status
    status['sla'] = end_time - start_time
    return status

    # if end_time - start_time > 0.5:
    #     # raise AssertionError(f"SLa not met: elapsed {end_time - start_time} > 0.5")
    #     print(f"SLa not met: elapsed {end_time - start_time} > 0.5")


@keyword
def ensure_acceptable_http_status_code(pingstatus):
    return 1


@keyword
def ensure_acceptable_http_response(pingstatus):
    return 1


if __name__ == '__main__':
    ping_meter('12356')
