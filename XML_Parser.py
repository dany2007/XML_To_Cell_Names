import xml.etree.ElementTree as ET
import csv

print("Drag an .XML file to extract cell names and ExternalId's")

fileRaw = input()
if fileRaw[0] == '"':
    file = fileRaw[1:-1]
else:
    file = fileRaw

outputFile = file[:-4] + ".csv"
tree = ET.parse(file)
root = tree.getroot()
children = list(root)

cellDict = {}

for cell in root.iter('RobcadStudy'):
    for content in list(cell):
        if content.tag == "name":
            cellDict[cell.attrib["ExternalId"]] = content.text

csv_columns = ['ExternalId', 'Cell Name']
csv_file = outputFile

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for key in cellDict.keys():
        csvfile.write("%s, %s\n" % (key, cellDict[key]))
