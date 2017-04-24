from django.conf.urls import url
from django.contrib import admin
from bt_scheduler.views import home, current_datetime, hours_ahead, contact, schedule

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', home),
    url(r'^contact/$', contact),
    url(r'^schedule/$', schedule)
]
