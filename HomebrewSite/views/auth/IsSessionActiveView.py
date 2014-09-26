from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore

class IsSessionActiveView(View):

    def get(self, request, *args, **kwargs):
        try:
            SessionStore(request["sessionID"])
        except KeyError:
            return HttpResponse('0')
        return HttpResponse('1')