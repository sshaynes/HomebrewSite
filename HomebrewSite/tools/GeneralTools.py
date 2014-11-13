import sys
import traceback

class GeneralTools:
	
	#takes exception info and returns a string to log
	@staticmethod
	def getExceptionInfo(sysinfo):
		exc_type, exc_value, exc_traceback = sysinfo
		return traceback.format_exception(exc_type, exc_value, exc_traceback)
		