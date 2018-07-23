from django.conf.urls import url
from django.contrib import admin
from bt_scheduler.views import home, current_datetime, hours_ahead, contact, schedule, display_meta, thankyou, location, class_detail

from books import views
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^schedule/location-(?P<abbrev>\w{0,20})/$', location),
    url(r'^schedule/class-(?P<abbrev>\w{0,20})/$', class_detail)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
