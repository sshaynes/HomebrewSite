from django.http import HttpResponse
from django.views.generic import View
from homebrew.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
import os
import sys

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreateUserView(View):

	@csrf_exempt
	def post(self, request, *args, **kwargs):

		# Make sure we're dealing with AJAX request
		if not request.is_ajax():
				return HttpResponseBadRequest('Expected an XMLHttpRequest')

		# Parse data from JSON
		data = json.loads(request.body)

		username = data.get('user','')
		if(username == ''):
			return HttpResponse('A username must be supplied')

		password = data.get('password','')
		if(password == ''):
			return HttpResponse('A password must be supplied')

		# Create and try to save the new user object
		user = User(username=username,password=password)
		try:
			user.save();
		except IntegrityError:
			return HttpResponse('Username is already taken!')
		except:
			return HttpResponse('Error saving user', sys.exc_info())


		# Create new user profile
		profile = Profile(user=user,
			age = data.get('age',''),
			location = data.get('location',''),
			name = data.get('name',''),
			yearsExperience = data.get('yearsExperience',''),
			avatarURL = data.get('avatarURL',''),
			reg_date=timezone.now(),
			update_date=timezone.now()
		)

		errorMsg = CreateUserView.validateProfile(profile)
		if errorMsg != '':
			return HttpResponse(errorMsg)
		logger.warning(profile)
		try:
			profile.save()
			response = 'Profile succesfully created'
		except:
			response = 'Profile failed to create with error: ', sys.exc_info()
		return HttpResponse(response)
		#return render(request, 'index.html', {}) may need this for csrf


	def get(self, request, *args, **kwargs):
		return HttpResponse('2b1189a188b44ad18c35e113ac6ceead')


	@staticmethod
	def validateProfile(profile):
		if profile.age == '':
			return 'age must be supplied'
		if profile.location == '':
			return 'location must be supplied'
		if profile.name == '':
			return 'name must be supplied'
		if profile.yearsExperience == '':
			return 'yearsExperience must be supplied'
		if profile.avatarURL == '':
			return 'avatarURL must be supplied'
		return ''