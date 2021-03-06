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
from django.core import serializers

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreateUserView(View):

	# @csrf_exempt
	def post(self, request, *args, **kwargs):

		# contType = "content_type='application/json'"

		# Parse data from JSON
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))
		username = data.get('user','')
		if(username == ''):
			return ApiTools.HttpJsonReponseMissingParameter('A username must be supplied')

		password = data.get('password','')
		if(password == ''):
			# return ApiTools.HttpJsonReponse('422', 'A password must be supplied')
			return ApiTools.HttpJsonReponseMissingParameter('A password must be supplied')

		email = data.get('email','')
		if(email == ''):
			return ApiTools.HttpJsonReponseMissingParameter('An email must be supplied')


		# Attempt to create and save the new user object
		# This method automatically hashes the password
		try:
			user = User.objects.create_user(username=username,password=password,email=email)
		except IntegrityError as e:
			return ApiTools.HttpJsonReponseBadRequest('Username is already taken!')
		except:
			return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))


		# Create new user profile
		profile = Profile(
			user=user,
			age = data.get('age',''),
			location = data.get('location',''),
			yearsExperience = data.get('yearsExperience',''),
			avatarURL = data.get('avatarURL',''),
			reg_date=timezone.now(),
			update_date=timezone.now()
		)

		errorMsg = CreateUserView.validateProfile(profile)
		if errorMsg != '':
			return ApiTools.HttpJsonReponseBadRequest(errorMsg)

		try:
			profile.save()
		except:
			return ApiTools.HttpJsonReponseBadRequest('Profile failed to create with error: ' + GeneralTools.getExceptionInfo(sys.exc_info()))
		
		return ApiTools.HttpJsonReponse(serializers.serialize('json', Profile.objects.filter(id=profile.id)))

		#return render(request, 'index.html', {}) may need this for csrf


	def get(self, request, *args, **kwargs):
		if(len(kwargs) == 1):
			#return the item passed in
			try:
				user = serializers.serialize('json', Profile.objects.filter(id=kwargs['pk']))
			except:
				return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))
		else:
			#return all objects
			user = serializers.serialize('json', Profile.objects.all())
		return ApiTools.HttpJsonReponseWithJsonData(user)


	@staticmethod
	def validateProfile(profile):
		if profile.age == '':
			return 'Age must be supplied.'
		if profile.location == '':
			return 'Location must be supplied.'
		if profile.yearsExperience == '':
			return 'YearsExperience must be supplied.'
		if profile.avatarURL == '':
			return 'AvatarURL must be supplied.'
		return ''
