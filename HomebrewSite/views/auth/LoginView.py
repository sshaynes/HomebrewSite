from django.http import HttpResponse
from django.views.generic import View

class LoginView(View):

	def get(self, request, *args, **kwargs):
		response = HttpResponse('2b1189a188b44ad18c35e113ac6ceead')
		return response