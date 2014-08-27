import xml.etree.ElementTree as ET
import os
import sys
import pymysql

pymysql.install_as_MySQLdb()
sys.path.insert(0, 'C:/Users/Drew/Documents/GitHub/HomebrewSite/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomebrewSite.settings")

from yeast import Yeast
from django.utils import timezone
from homebrew.models import Yeast

tree = ET.parse('Yeast_XML.xml')
root = tree.getroot()

listOfYeast = []
yeast = Yeast()

for element in root.iter('*'):
	if element.tag == "YEAST":
		if yeast.name != "":
			listOfYeast.append(yeast)
			yeast = Yeast()
	elif element.tag == "NAME":
		yeast.name = element.text
	elif element.tag == "TYPE":
		yeast.type = element.text	
	elif element.tag == "FORM":
		yeast.form = element.text
	elif element.tag == "AMOUNT":
		yeast.amount = element.text
	elif element.tag == "AMOUNT_IS_WEIGHT":
		yeast.amount_is_weight = element.text
	elif element.tag == "LABORATORY":
		yeast.laboratory = element.text
	elif element.tag == "PRODUCT_ID":
		yeast.product_id = element.text
	elif element.tag == "MIN_TEMPERATURE":
		yeast.min_temperature = element.text
	elif element.tag == "MAX_TEMPERATURE":
		yeast.max_temperature = element.text
	elif element.tag == "FLOCCULATION":
		yeast.flocculation = element.text
	elif element.tag == "ATTENUATION":
		yeast.attenuation = element.text
	elif element.tag == "NOTES":
		yeast.notes = element.text
	elif element.tag == "BEST_FOR":
		yeast.best_for = element.text
	elif element.tag == "TIMES_CULTURED":
		yeast.times_cultured = element.text
	elif element.tag == "MAX_REUSE":
		yeast.max_reuse = element.text		
	elif element.tag == "ADD_TO_SECONDARY":
		yeast.add_to_secondary = element.text
	elif element.tag == "DISPLAY_AMOUNT":
		yeast.display_amount = element.text
	elif element.tag == "DISP_MIN_TEMP":
		yeast.disp_min_temp = element.text	
	elif element.tag == "DISP_MAX_TEMP":
		yeast.disp_max_temp = element.text	

for item in listOfYeast:
	yeastToSave = Yeast(name=item.name, type=item.type, form=item.form, amount=item.amount, amount_is_weight=item.amount_is_weight,
	laboratory=item.laboratory, product_id=item.product_id, min_temperature=item.min_temperature, max_temperature=item.max_temperature,
	flocculation=item.flocculation, attenuation=item.attenuation, notes=item.notes, best_for=item.best_for, times_cultured=item.times_cultured,
	max_reuse=item.max_reuse, add_to_secondary=item.add_to_secondary, display_amount=item.display_amount, disp_min_temp=item.disp_min_temp,
	disp_max_temp=item.disp_max_temp, pub_date=timezone.now());
	yeastToSave.save();
		
