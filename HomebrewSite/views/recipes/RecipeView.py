from django.http import HttpResponse
from django.views.generic import View
from homebrew.models import Profile
from django.contrib.auth.models import User
from homebrew.models import Recipe
from HomebrewSite.views.recipes.recipes import Recipes
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

class RecipeView(View):

	def get(self, request, *args, **kwargs):
		if(len(kwargs) == 1):
			#return the item passed in
			try:
				recipe = serializers.serialize('json', Recipe.objects.filter(id=kwargs['pk']))
			except:
				return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))
		else:
			#return all objects
			recipe = serializers.serialize('json',Recipe.objects.all())
		return ApiTools.HttpJsonReponseWithJsonData(recipe);

	def patch(self, request, *args, **kwargs):
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))
		recipe = Recipe.objects.filter(id=data.get('id'))
		recipe.userid = data.get('userid','')
		recipe.styleid = data.get('styleid','')
		recipe.substyleid = data.get('substyleid','')
		recipe.description = data.get('description','')
		recipe.boilTime = data.get('boilTime','')
		recipe.units = data.get('units','')
		recipe.method = data.get('method','')
		recipe.batchSize = data.get('batchSize','')
		recipe.boilSize = data.get('boilSize','')
		recipe.id = data.get('id','')
		recipe.abv = data.get('abv','')
		recipe.ibu = data.get('ibu','')
		recipe.name = data.get('name','')
		recipe.save();

	def post(self, request, *args, **kwargs):
		# contType = "content_type='application/json'"

		# Parse data from JSON
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponseBadRequest(GeneralTools.getExceptionInfo(sys.exc_info()))

		useridi = data.get('userid','')
		styleidi = data.get('styleid','')
		substyleidi = data.get('substyleid','')
		descriptioni = data.get('description','')
		boilTimei = data.get('boilTime','')
		unitsi = data.get('units','')
		methodi = data.get('method','')
		batchSizei = data.get('batchSize','')
		boilSizei = data.get('boilSize','')
		#id = data.get('id','') will be supplied
		abvi = data.get('abv','')
		ibui = data.get('ibu','')
		namei = data.get('name','')

		user_idi = request.user.id;
		if(user_idi == None):
			user_idi = 1; # for testing, should throw an exception here
		if(namei == ''):
			return ApiTools.HttpJsonReponseMissingParameter('A name must be supplied')
		recipeToSave = Recipe(userid=useridi, styleid=styleidi, substyleid=substyleidi, description=descriptioni, boilTime=boilTimei, units=unitsi,
		method=methodi, batchSize=batchSizei, boilSize=boilSizei, abv=abvi, ibu=ibui, name=namei, user_id=user_idi, pub_date=timezone.now());
		recipeToSave.save();
		return ApiTools.HttpJsonReponse("success");