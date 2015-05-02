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
import uuid
from django.utils import timezone
from HomebrewSite.tools.ApiTools import ApiTools
from HomebrewSite.tools.GeneralTools import GeneralTools

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RecipeView(View):

	def get(self, request, *args, **kwargs):
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponse('400', GeneralTools.getExceptionInfo(sys.exc_info()))
		
		recipe = Recipe.objects.filter(id=data.get('id'))
		logger.warning(recipe)
		ApiTools.HttpJsonReponse("here");
		
	def patch(self, request, *args, **kwargs):
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponse('400', GeneralTools.getExceptionInfo(sys.exc_info()))
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

		# Make sure we're dealing with AJAX request
		if not request.is_ajax():
				return HttpResponse('Expected an XMLHttpRequest')

		# Parse data from JSON
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			logger.warning(GeneralTools.getExceptionInfo(sys.exc_info()))
			return ApiTools.HttpJsonReponse('400', GeneralTools.getExceptionInfo(sys.exc_info()))
		logger.warning(data)

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

		if(name == ''):
			return ApiTools.HttpJsonReponse('422', 'A name must be supplied')
		
		recipeToSave = Recipes(userid=useridi, styleid=styleidi, substyleid=substyleidi, description=descriptioni, boilTime=boilTimei, units=unitsi,
		method=methodi, batchSize=batchSizei, boilSize=boilSizei, abv=abv, ibu=ibui, namei=name, id=uuid.uuid4());
		recipeToSave.save();