from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from bt_scheduler.forms import ContactForm
from django.db import models
from events.models import Message, Event, Location, Class

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
    prior_date = datetime.datetime.now() - datetime.timedelta(days=7)
    future_date = datetime.datetime.now() + datetime.timedelta(days=7)
    event_list = Event.objects.filter(start_time__gte=prior_date, start_time__lte=future_date)
    event_hash_list = []
    for event in event_list:
	event_hash_list.append(hash_event(event))
    return render(request, 'schedule.html', {'events': event_hash_list})

def location(request, abbrev):
    prior_date = datetime.datetime.now() - datetime.timedelta(days=7)
    future_date = datetime.datetime.now() + datetime.timedelta(days=7)
    event_list = Event.objects.filter(start_time__gte=prior_date, end_time__lte=future_date)
    event_hash_list = []
    for event in event_list:
	event_hash_list.append(hash_event(event))
    location = Location.objects.filter(abbreviation=abbrev) 
    if len(location) == 0:
	raise Http404()
    return render(request, 'schedule.html', {'events': event_hash_list, 'location': location[0]})

def class_detail(request, abbrev):
    prior_date = datetime.datetime.now() - datetime.timedelta(days=7)
    future_date = datetime.datetime.now() + datetime.timedelta(days=7)
    event_list = Event.objects.filter(start_time__gte=prior_date, end_time__lte=future_date)
    event_hash_list = []
    for event in event_list:
	event_hash_list.append(hash_event(event))
    class_type = Class.objects.filter(abbreviation=abbrev) 
    if len(class_type) == 0:
        class_type=['not-found']	
    return render(request, 'schedule.html', {'events': event_hash_list, 'class_type': class_type[0]})
def thankyou(request):
    return render(request, 'thank-you.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
	    #temp solution
	    msg = Message.objects.create(subject=cd['subject'],email=cd['email'],content=cd['message'],timesent=datetime.datetime.now())    
	    #end temp solution
            #send_mail(
            #    cd['subject'],
	    #	cd['message'],
	    #	cd.get('email', 'noreply@example.com'), ['siteowner@example.com'],
	    #)
	    
	    return HttpResponseRedirect('/contact/thank-you/')
    else:
	form = ContactForm(initial={'subject': 'Hi'})
    return render(request, 'contact.html',{'form': form})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hash_event(event):
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return {'start_time': event.start_time.time ,'end_time': event.end_time.time, 'date': event.start_time.date, 'weekday': weekdays[event.start_time.weekday()], 'month': months[event.start_time.month], 'location': event.location, 'original': event, 'class_type': event.class_type}
