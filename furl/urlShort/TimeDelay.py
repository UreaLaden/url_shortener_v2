from http.client import HTTPResponse
import time
from django.conf import settings

class TimeDelayMiddleware(object):
    def __init__(self,get_response:HTTPResponse):
        self.get_response = get_response
        self.delay = settings.REQUEST_TIME_DELAY

    def __call__(self,request):
        if 'go' in request.path:
            time.sleep(self.delay)
        response:HTTPResponse = self.get_response(request)
        return response