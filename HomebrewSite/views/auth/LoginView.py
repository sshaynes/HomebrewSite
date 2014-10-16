from django.http import HttpResponse
from django.utils.html import escape
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
from HomebrewSite.tools.DateTools import DateTools
import json
import datetime
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class LoginView(View):

	def get(self, request, *args, **kwargs):
		#pending successful login
		s = SessionStore()
		s['last_login'] = DateTools.getNowAsString()
		s['userid'] = 1	#this should be set to the user id returned from authentication
		s.save()
		response = s.session_key + " | Last_login: " + s['last_login']

		return HttpResponse(response)


	def post(self, request, *args, **kwargs):

		#pending successful login
		s = SessionStore()
		s['last_login'] = DateTools.getNowAsString()
		s['userid'] = 1	#this should be set to the user id returned from authentication
		s.save()
		response = s.session_key + " | Last_login: " + s['last_login']

		return HttpResponse(response)
