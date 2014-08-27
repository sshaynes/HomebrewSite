import xml.etree.ElementTree as ET
import os
import sys
import pymysql

pymysql.install_as_MySQLdb()
sys.path.insert(0, 'C:/Users/Drew/Documents/GitHub/HomebrewSite/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomebrewSite.settings")

from hops import Hops
from django.utils import timezone
from homebrew.models import Hop



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
	hopToSave = Hop(origin=item.origin, time=item.time, notes=item.notes, alpha=item.alpha, amount=item.amount,
	use=item.use, displayAmount=item.displayAmount, type=item.type, beta=item.beta, form=item.form, displayTime=item.displayTime,
	name=item.name, hsi=item.hsi, pub_date=timezone.now());
	hopToSave.save();
		
