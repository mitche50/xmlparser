import xml.etree.ElementTree as ET
from datetime import datetime

tree = ET.parse('input.xml')

root = tree.getroot()
f = open('output.txt', 'w')

f.write("usage point,occurred,value\n")

for child in root.findall('.//{http://www.w3.org/2005/Atom}content'):
    usage_point = child[0].tag
    if child.findall(".//{http://naesb.org/espi}start") or child.findall(".//{http://naesb.org/espi}value"):
        f.write(usage_point + ",None,None\n")
        for item in child[0]:
            usage_point = item.tag
            start, value = "None", "None"
            if item.findall("{http://naesb.org/espi}start"):
                start = item.find("{http://naesb.org/espi}start").text
            if item.findall("{http://naesb.org/espi}value"):
                value = item.find("{http://naesb.org/espi}value").text
            if item.findall('{http://naesb.org/espi}timePeriod'):
                for time in item.find("{http://naesb.org/espi}timePeriod"):
                    if time.tag == "{http://naesb.org/espi}start":
                        start = time.text
            if start != "None":
                start = datetime.utcfromtimestamp(int(start)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

            f.write(usage_point + "," + str(start) + "," + str(value) + "\n")
    else:
        f.write(usage_point + ",None,None\n")
