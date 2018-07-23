# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Event, Instructor, Student, Message, Location, Class, Announcement, Quote, Document

admin.site.register(Event)
admin.site.register(Instructor)
admin.site.register(Student) 
admin.site.register(Message)
admin.site.register(Location)
admin.site.register(Class)
admin.site.register(Announcement)
admin.site.register(Quote)
admin.site.register(Document)

# Register your models here.
