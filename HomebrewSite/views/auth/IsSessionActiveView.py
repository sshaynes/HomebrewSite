from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
import logging

class IsSessionActiveView(View):

    def get(self, request, *args, **kwargs):
        try:
            s = SessionStore(request.GET["sessionID"])
            if s['userid'] != "":
                return HttpResponse('1')
            else:
                return HttpResponse('0')
        except:# KeyError:
            return HttpResponse('0')