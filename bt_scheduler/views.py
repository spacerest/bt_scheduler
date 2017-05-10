from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from bt_scheduler.forms import ContactForm
from django.db import models
from events.models import Message

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
