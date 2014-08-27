import xml.etree.ElementTree as ET
import os
import sys
import pymysql

pymysql.install_as_MySQLdb()
sys.path.insert(0, 'C:/Users/Drew/Documents/GitHub/HomebrewSite/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomebrewSite.settings")

from grains import Grains
from django.utils import timezone
from homebrew.models import Grain

tree = ET.parse('Grain_XML.xml')
root = tree.getroot()

listOfGrains = []
grain = Grains()

for element in root.iter('*'):
	if element.tag == "FERMENTABLE":
		if grain.name != "":
			listOfGrains.append(grain)
			grain = Grains()
	elif element.tag == "ORIGIN":
		grain.origin = element.text
	elif element.tag == "RECOMMEND_MASH":
		grain.recommendMash = element.text	
	elif element.tag == "NOTES":
		grain.notes = element.text
	elif element.tag == "ADD_AFTER_BOIL":
		grain.addAfterBoil = element.text
	elif element.tag == "AMOUNT":
		grain.amount = element.text
	elif element.tag == "MAX_IN_BATCH":
		grain.maxInBatch = element.text
	elif element.tag == "DISPLAY_AMOUNT":
		grain.displayAmount = element.text
	elif element.tag == "TYPE":
		grain.type = element.text
	elif element.tag == "PROTEIN":
		grain.protein = element.text
	elif element.tag == "SUPPLIER":
		grain.supplier = element.text
	elif element.tag == "DISPLAY_COLOR":
		grain.displayColor = element.text
	elif element.tag == "NAME":
		grain.name = element.text
	elif element.tag == "POTENTIAL":
		grain.potential = element.text
	elif element.tag == "MOISTURE":
		grain.moisture = element.text
	elif element.tag == "COARSE_FINE_DIFF":
		grain.coarseFineDiff = element.text		
	elif element.tag == "COLOR":
		grain.color = element.text
	elif element.tag == "EXTRACT_SUBSTITUTE":
		grain.extractSubstitue = element.text
	elif element.tag == "DIASTATIC_POWER":
		grain.diastaticPower = element.text	
	elif element.tag == "IBU_GAL_PER_LB":
		grain.ibuGalPerLb = element.text	
	elif element.tag == "YIELD":
		grain.yeild = element.text	

for item in listOfGrains:
	grainToSave = Grain(origin=item.origin, recommendMash=item.recommendMash, notes=item.notes, addAfterBoil=item.addAfterBoil,
	amount=item.amount, maxInBatch=item.maxInBatch, displayAmount=item.displayAmount, protein=item.protein, type=item.type,
	supplier=item.supplier, displayColor=item.displayColor, name=item.name, potential=item.potential, moisture=item.moisture,
	coarseFineDiff=item.coarseFineDiff, color=item.color, extractSubstitue=item.extractSubstitue, diastaticPower=item.diastaticPower,
	ibuGalPerLb=item.ibuGalPerLb, yeild=item.yeild, pub_date=timezone.now());
	grainToSave.save();
		
