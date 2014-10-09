from django.http import HttpResponse
from django.views.generic import View
from homebrew.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import os
import sys

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CreateUserView(View):
	@csrf_exempt
	def post(self, request, *args, **kwargs):
		username = request.POST.get('user','')
		password = request.POST.get('password','')
		if(username == ''):
			return HttpResponse('A username must be supplied')
		if(password == ''):
			return HttpResponse('A password must be supplied')
		user = User(username=username,password=password)
		profile = Profile(user=user,
		age = request.POST.get('age',''),
		location = request.POST.get('location',''),
		name = request.POST.get('name',''),
		yearsExperience = request.POST.get('yearsExperience',''),
		avatarURL = request.POST.get('avatarURL',''))
		errorMsg = validateProfile(profile)
		if errorMsg != '':
			return HttpResponse(errorMsg)
		logger.warning(profile)
		try:
			profile.save()
			respone = 'Profile succesfully created'
		except:
			respone = 'Profile failed to create with error: ', sys.exc_info()[0]
		return HttpResponse(response)
		#return render(request, 'index.html', {}) may need this for csrf
		
	def get(self, request, *args, **kwargs):
		return HttpResponse('2b1189a188b44ad18c35e113ac6ceead')
	
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