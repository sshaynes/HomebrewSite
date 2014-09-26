from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        try:
            s = SessionStore(request["sessionID"])
        except KeyError:
            return HttpResponse('0')
        s.set_expiry(1) #set the session to expire in 1 second, 0 would make it never expire
        return HttpResponse('1')