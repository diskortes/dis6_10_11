'''
Created on 06.10.2011

@author: Server
'''

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
import datetime

def hello(request):
    return HttpResponse("Hello DIS!")

def current_time(request):
    now = datetime.datetime.now()
    t = get_template('current_time.html')
    a = Context()
    a['current_date'] = now
    html = t.render(a)
    return HttpResponse(html)

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