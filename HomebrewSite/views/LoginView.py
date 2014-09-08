from django.http import HttpResponse
from django.views.generic import View

class LoginView(View):

	def get(self, *args, **kwargs):
		response = HttpResponse('hello world')
		return response