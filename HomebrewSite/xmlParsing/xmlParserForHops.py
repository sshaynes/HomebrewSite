import xml.etree.ElementTree as ET
from hops import Hops

tree = ET.parse('Hops_XML.xml')
root = tree.getroot()

listOfHops = []
hop = Hops()
for element in root.iter('*'):
	if element.tag == "HOP":
		if hop.name != "":
			listOfHops.append(hop)
			hop = Hops()
	elif element.tag == "ORIGIN":
		hop.origin = element.text
	elif element.tag == "TIME":
		hop.time = element.text	
	elif element.tag == "NOTES":
		hop.notes = element.text
	elif element.tag == "ALPHA":
		hop.alpha = element.text
	elif element.tag == "AMOUNT":
		hop.amount = element.text
	elif element.tag == "USE":
		hop.use = element.text
	elif element.tag == "DISPLAY_AMOUNT":
		hop.displayAmount = element.text
	elif element.tag == "TYPE":
		hop.type = element.text
	elif element.tag == "BETA":
		hop.beta = element.text
	elif element.tag == "FORM":
		hop.form = element.text
	elif element.tag == "DISPLAY_TIME":
		hop.displayTime = element.text
	elif element.tag == "NAME":
		hop.name = element.text
	elif element.tag == "HSI":
		hop.hsi = element.text
		
for item in listOfHops:
	print(item)
		
