'''
Created on 06.10.2011

@author: Server
'''

from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello DIS!")

def current_time(request):
    now ="<html><h2>Now %s</h2></html>" % datetime.datetime.now()
    return HttpResponse(now)

def time_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "After %s hours will be %s" % (offset, dt)
    return HttpResponse(html)    

def plus (request):
    return HttpResponse("PLUS+")