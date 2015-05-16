from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
import json

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ApiTools:

  # Returns Status 200 OK
  @staticmethod
  def HttpJsonReponse(message):
    status = 200;
    data = {'status': 200, 'message': message}
    return HttpResponse(json.dumps(data))


  # Returns Status 400
  @staticmethod
  def HttpJsonReponseBadRequest(message):
    status = 400
    data = {'status': status, 'message': message}
    return HttpResponseBadRequest(json.dumps(data))


  # Returns Status 400
  @staticmethod
  def HttpJsonReponseMissingParameter(message):
    status = 400
    data = {'status': status, 'message': message}
    return HttpResponse(json.dumps(data), status=400)


  # Returns Status 401
  @staticmethod
  def HttpJsonReponseUnauthorized(message):
    status = 401
    data = {'status': status, 'message': message}
    return HttpResponse(json.dumps(data), status=status)


  # Returns Status 403
  @staticmethod
  def HttpJsonResponseForbidden(message):
    status = 403
    data = {'status': status, 'message': message}
    return HttpResponseForbidden(json.dumps(data))


  # Returns Status 404
  @staticmethod
  def HttpJsonResponseNotFound(message):
    status = 404
    data = {'status': status, 'message': message}
    return HttpResponseNotFound(json.dumps(data))


