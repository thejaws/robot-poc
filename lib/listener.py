from lxml import etree
from multiprocessing import Process
from robot.api.deco import keyword
from flask import Flask
from flask import request
import xml.dom.minidom

app = Flask(__name__)
server = False

ROBOT_AUTO_KEYWORDS = False

@app.route('/', defaults={'path': ''}, methods=['GET','POST'])
@app.route('/<path:path>',methods=['GET','POST'])
def catch_all(path):
    data = request.data
    print(data.__class__)
    print('now dom')
    dom = xml.dom.minidom.parseString(data)
    root = etree.fromstring(data)
    result = etree.tostring(root, pretty_print = True, method = "xml")
    print("===== pretty")
    print(str(result))
    print("<==== <<<<< ======")
    corr_id = root.find('.//mes:CorrelationId')
    # print('preety:')
    # pretty_xml_as_string = dom.toprettyxml().replace("\n\n", "\n").replace("\r\n", "\n")
    # print(pretty_xml_as_string)
    return 'You want path: %s' % path

@keyword
def start_listener():
    server = Process(target=app.run(host='0.0.0.0', port=50999))
    server.start()


@keyword
@app.route('/shutit')
def stop_listener():
    server.terminate()
    server.join()

if __name__ == "__main__":
    start_listener()
