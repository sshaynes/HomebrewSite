from django.http import HttpResponse
from django.utils.html import escape
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import authenticate, login
from HomebrewSite.tools.DateTools import DateTools
from HomebrewSite.tools.ApiTools import ApiTools
from HomebrewSite.tools.GeneralTools import GeneralTools

import json
import datetime
# import the logging library
import logging
import sys

# Get an instance of a logger
logger = logging.getLogger(__name__)

class LoginView(View):

	def get(self, request, *args, **kwargs):
		#what does a get do here?
		s = SessionStore()
		s['last_login'] = DateTools.getNowAsString()
		s['userid'] = 1 #this should be set to the user id returned from authentication
		s.save()
		response = s.session_key + " | Last_login: " + s['last_login']

		return HttpResponse(response)


	def post(self, request, *args, **kwargs):
		# contType = "content_type='application/json'"

		# Make sure we're dealing with AJAX request
		if not request.is_ajax():
				return HttpJsonReponseBadRequest('Expected an XMLHttpRequest')

		# Parse data from JSON
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))
		logger.warning(data)

		# return ApiTools.HttpJsonReponse('500', request.body);

		username = data.get('user','')

		if(username == ''):
			return ApiTools.HttpJsonReponseMissingParameter('A username must be supplied')
		#how are we passing password? I know not flattext but I wonder how we handle logging in here.
		password = data.get('password','')
		if(password == ''):
			return ApiTools.HttpJsonReponseMissingParameter('A password must be supplied')

		user = authenticate(username=username, password=password)
		# If username/password combo is invalid it returns 'None'
		if user is not None:
			if user.is_active:
				#do we want to redirect to another page here or just return a session and have the UI handle it?
				login(request, user)
				s = SessionStore()
				s['last_login'] = DateTools.getNowAsString()
				s['userid'] = user.username
				s.save()
				return ApiTools.HttpJsonReponse('Login successful!')
			else:
				# Will we ever have inactive users?
				return ApiTools.HttpJsonReponseUnauthorized('Inactive user')

		else:
			return ApiTools.HttpJsonReponseUnauthorized('Invalid username or password')
