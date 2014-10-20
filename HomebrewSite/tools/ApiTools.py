from django.http import HttpResponse
import json

class ApiTools:

  @staticmethod
  def HttpJsonReponse(status, message):
    data = {'status': status, 'message': message}
    return HttpResponse(json.dumps(data), content_type='application/json')