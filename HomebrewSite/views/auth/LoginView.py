from django.http import HttpResponse
from django.utils.html import escape
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
import json
import datetime

class LoginView(View):

	def get(self, request, *args, **kwargs):

		#pending successful login
		s = SessionStore()
		s['last_login'] = datetime.datetime.now()
		s['userid'] = 1	#this should be set to the user id returned from authentication
		s.save()
		response = s.session_key
		response += '_GET'

		response = repr(request.GET)
		# response = json.loads(request.GET)

		response = HttpResponse(response)
		return response


	def post(self, request, *args, **kwargs):

		#pending successful login
		s = SessionStore()
		s['last_login'] = datetime.datetime.now()
		s['userid'] = 1	#this should be set to the user id returned from authentication
		s.save()
		response = s.session_key
		response += '_POST'

		response = repr(request.body)
		response = HttpResponse(response)

		# response = json.loads(request.body)
		# response = HttpResponse(response[0])

		return response