from django.conf.urls import url
from django.contrib import admin
from bt_scheduler.views import home, current_datetime, hours_ahead, contact, schedule, display_meta, thankyou

from books import views

urlpatterns = [
    url(r'^here/', admin.site.urls),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', home),
    url(r'^contact/$', contact),
    url(r'^schedule/$', schedule),
    url(r'^display_meta/$', display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/thank-you/$', thankyou),
]
