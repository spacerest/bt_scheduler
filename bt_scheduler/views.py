from django.http import HttpResponse
from django.shortcuts import render
import datetime

def current_datetime(request): 
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)

def home(request):
    return render(request, 'index.html', {})

def schedule(request):
    return render(request, 'schedule.html', {})

def contact(request):
    return render(request, 'contact.html',{})
