from django.http import HttpResponse
from django.views.generic import View

class DeleteUserView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('1')