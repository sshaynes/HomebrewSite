from django.http import HttpResponse
from django.views.generic import View
from homebrew.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
import os
import sys
import datetime
from django.utils import timezone
from HomebrewSite.tools.ApiTools import ApiTools
from HomebrewSite.tools.GeneralTools import GeneralTools

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreateUserView(View):

	# @csrf_exempt
	def post(self, request, *args, **kwargs):

		# contType = "content_type='application/json'"

		# Make sure we're dealing with AJAX request
		if not request.is_ajax():
				return HttpResponse('Expected an XMLHttpRequest')
		# Parse data from JSON
		data = json.loads(request.body.decode("utf-8"))
		username = data.get('user','')
		if(username == ''):
			return ApiTools.HttpJsonReponse('422', 'A username must be supplied')

		password = data.get('password','')
		if(password == ''):
			return ApiTools.HttpJsonReponse('422', 'A password must be supplied')

		email = data.get('email','')
		if(email == ''):
			return ApiTools.HttpJsonReponse('422', 'An email must be supplied')


		# Attempt to create and save the new user object
		# This method automatically hashes the password
		try:
			user = User.objects.create_user(username=username,password=password,email=email)
			user.save();
		except IntegrityError as e:
			return ApiTools.HttpJsonReponse('422', 'Username is already taken!')
		except:
			return ApiTools.HttpJsonReponse('400', GeneralTools.getExceptionInfo(sys.exc_info()))


		# Create new user profile
		profile = Profile(user=user,
			age = data.get('age',''),
			location = data.get('location',''),
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
			# profile.save()
			return ApiTools.HttpJsonReponse('200', 'Profile successfully created')
		except:
			return ApiTools.HttpJsonReponse('400', 'Profile failed to create with error: ' + GeneralTools.getExceptionInfo(sys.exc_info()))

		#return render(request, 'index.html', {}) may need this for csrf


	def get(self, request, *args, **kwargs):
		ApiTools.HttpJsonReponse('200', '2b1189a188b44ad18c35e113ac6ceead')


	@staticmethod
	def validateProfile(profile):
		if profile.age == '':
			return 'age must be supplied'
		if profile.location == '':
			return 'location must be supplied'
		if profile.yearsExperience == '':
			return 'yearsExperience must be supplied'
		if profile.avatarURL == '':
			return 'avatarURL must be supplied'
		return ''
