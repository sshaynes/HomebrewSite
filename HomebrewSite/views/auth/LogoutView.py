from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import logout
import logging

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        try:
            s = SessionStore(request.GET["sessionID"])
            if s['userid'] == "":
                logging.error("session is inactive")
                return HttpResponse('0')
        except KeyError:
            logging.error("key error")
            return HttpResponse('0')
        logout(request)
        s.set_expiry(1) #set the session to expire in 1 second, 0 would make it never expire
        logging.warning(s.get_expiry_date())		
        return HttpResponse('1')