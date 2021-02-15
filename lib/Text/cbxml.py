import xml.etree.ElementTree as ET

tree = ET.parse('cb.xml')
root = tree.getroot()
# root = ET.fromstring(country_data_as_string)
print(root)
print('---')
print(tree)

print('findall: --->')
# for e in root.findall('{http://iec.ch/TC57/2007/EndDeviceEvent#}EndDeviceEvent'):
def recurse(elem, level):
    level +=1
    print(f"{level*' '} {elem} \n  {level*' '} {elem.text}")
    for children in elem:
        recurse(children, level)


recurse(root, 0)

# for item in root:
#     print('-')
#     print(item)
#     for cw in item:
#         print(cw)
#         print(cw.text)
#         print('--^^--')
#
# print('<----')
res = root.findall('.//{http://iec.ch/TC57/2011/schema/message}CorrelationID')
print(res)