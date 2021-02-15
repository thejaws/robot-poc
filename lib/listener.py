import xml.etree.ElementTree as ET
from robot.api.deco import keyword
from flask import Flask
from flask import request

app = Flask(__name__)
server = False

ROBOT_AUTO_KEYWORDS = False

messages = {}


@app.route('/corrid')
def corrid():
    return messages[corrid]


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    data = request.data
    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    xml_string = ET.tostring(root, 'utf-8').decode("utf-8")
    print(xml_string)

    print('--- --- --- --- ')
    namespaces = {'mes': 'http://iec.ch/TC57/2011/schema/message'}
    for c in tree.findall('CorrelationID'):
        print('-')
        print(c)
        print(c.text)
    print("<==== <<<<< ======")
    # corr_id = root.find('.//CorrelationID')
    res = root.findall('.//{http://iec.ch/TC57/2011/schema/message}CorrelationID')
    # print(res)
    # print(res[0].text)
    messages[res[0].text] = xml_string

    print(messages)
    return 'You want path: %s' % path


@keyword
def start_listener():
    # server = Process(target=app.run(host='0.0.0.0', port=50999))
    # server.start()
    app.run(debug=True, port=50999)


@keyword
@app.route('/shutit')
def stop_listener():
    server.terminate()
    server.join()


if __name__ == "__main__":
    start_listener()
