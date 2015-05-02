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


class UserAndProfileInfoAPI(View):
	def get(self, request, *args, **kwargs):
		s = SessionStore()