# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Event, Instructor, Student

admin.site.register(Event)
admin.site.register(Instructor)
admin.site.register(Student) 

# Register your models here.
