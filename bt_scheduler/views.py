from django.http import HttpResponse
from django.shortcuts import render
import datetime
import random
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from bt_scheduler.forms import ContactForm
from django.db import models
from events.models import Message, Event, Location, Class, Announcement, Quote, Document

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
    announcement_list = Announcement.objects.all()
    prior_date = datetime.datetime.now() - datetime.timedelta(days=7)
    future_date = datetime.datetime.now() + datetime.timedelta(days=7)
    quotes_list = Quote.objects.all()
    if (len(quotes_list) > 0):
        quote = random.choice(quotes_list)
    else:
        quote = ""
    event_list = Event.objects.all().filter(show_this_event=True)
    event_hash_list = []
    for event in event_list:
	event_hash_list.append(hash_event(event))
    return render(request, 'schedule.html', {'events': event_hash_list, 'announcements': announcement_list, 'quote':quote})

def location(request, abbrev):
    prior_date = datetime.datetime.now() - datetime.timedelta(days=7)
    future_date = datetime.datetime.now() + datetime.timedelta(days=7)
    event_list = Event.objects.all()
    event_list = Event.objects.all().filter(show_this_event=True)
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
    event_list = Event.objects.all()
    event_list = Event.objects.all().filter(show_this_event=True)
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
    announcement_list = Announcement.objects.all()
    documents = Document.objects.all()
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
	form = ContactForm(initial={'subject': ''})
    return render(request, 'contact.html',{'announcements': announcement_list, 'form': form, 'documents': documents})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hash_event(event):
    return {'location': event.location, 'original': event, 'class_type': event.class_type}
