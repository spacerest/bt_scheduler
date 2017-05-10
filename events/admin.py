# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Event, Instructor, Student, Message

admin.site.register(Event)
admin.site.register(Instructor)
admin.site.register(Student) 
admin.site.register(Message)

# Register your models here.
