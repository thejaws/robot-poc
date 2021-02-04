import requests
from robot.api.deco import keyword
from mako.template import Template
import re

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


ROBOT_AUTO_KEYWORDS = False
from amst_db import get_communicating_meter_cbconnected_localdisconnect_enabled

def get_template():
   return Template(filename='lib/Text/cb.txt')

def get_url_headers():
    headers = {'content-type': 'text/xml',
               'SOAPAction': 'http://aidon.com/IEC/AdHoc/v4/IECAdHocPortType/ExecuteCircuitBreakerControlRequest'
               }

    url = "https://172.19.1.205:50100/IECAdHoc/IECAdHoc.svc"
    url = "http://localhost:50999/xmltest"

    return url, headers


def verify_synch_response(response):
    print(response.url)
    print(response.headers)
    print(response.text)
    failed = False
    reasons = ''
    failure_description = 'No failure'
    pattern = re.compile(r'\>(\w+)\<\/Result')
    res = pattern.search(response.text)
    if res is not None:
        if res.group(1) == 'FAILED':
            failed = True
            reasons_pat = re.compile(r'reason.*details')
            reasons_res = reasons_pat.search(response.text)
            reasons = reasons_res.group(0)
            failure_description = res.group(0) + " ===> " + reasons

    if failed is True:
        raise AssertionError(failure_description)


@keyword
def select_meter(cbstatus, commstatus):
    (meterpoint, meter) = get_communicating_meter_cbconnected_localdisconnect_enabled()
    return (meterpoint, meter)


@keyword
def ensure_cb(mp_meter):
    print("ensure> ")
    print(mp_meter)
    return "user"

@keyword
def set_circuitbreaker_status(minfo, status):
    device, meterpoint = minfo

    mytemplate = get_template()
    payload_org = """
         <end:Payload>
            <end:EndDeviceControl>
               <end1:EndDeviceAction>
                  <end1:command>${status}</end1:command>
               </end1:EndDeviceAction>
            </end:EndDeviceControl>
         </end:Payload>
    """
    payload_template = Template(payload_org)
    payload = payload_template.render(status=status)
    print("Payload: ")
    print(payload)

    body = mytemplate.render(meterpoint=meterpoint,payload=payload)
    print("BODY")
    print(body)
    print("\n\n\n======")

    url, headers = get_url_headers()
    response = requests.post(url, data=body, headers=headers, verify=False)
    print(response)
    print(response.url)
    print(response.headers)
    print(response.text)
    print("cb status ====================")


@keyword
def read_circuitbreaker_status(m_info):
    device, meterpoint = m_info
    mytemplate = get_template()
    url, headers = get_url_headers()
    body = mytemplate.render(meterpoint=meterpoint,payload='')
    print(body)
    print("\n\n\n======")
    response = requests.post(url, data=body, headers=headers, verify=False)
    verify_synch_response(response)


if __name__ == "__main__":
    print("retval = ")
    read_circuitbreaker_status(('735xxxp000','7320630188057'))
