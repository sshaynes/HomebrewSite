import json
import datetime

class DateTools:
	#takes in python datetime, returns a string in ISO 8601 format
	@staticmethod
	def datetimeToString(date):
		return date.isoformat()

	#returns right now as an ISO 8601 string
	@staticmethod
	def getNowAsString():
		return datetime.datetime.now().isoformat()