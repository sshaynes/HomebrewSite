from django.http import HttpResponse
from django.utils.html import escape
from django.views.generic import View
import json

class LoginView(View):

	def get(self, request, *args, **kwargs):

		response = '6UjKyxZXtVOkLzKMr3oyxb1gF2X4VWhY'
		response += '_GET'

		response = repr(request.GET)
		# response = json.loads(request.GET)

		response = HttpResponse(response)
		return response


	def post(self, request, *args, **kwargs):

		response = '6UjKyxZXtVOkLzKMr3oyxb1gF2X4VWhY'
		response += '_POST'

		response = repr(request.body)
		response = HttpResponse(response)

		# response = json.loads(request.body)
		# response = HttpResponse(response[0])

		return response