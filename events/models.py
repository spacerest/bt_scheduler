# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    def __str__(self):
	return self.first_name + " " + self.last_name


class Event(models.Model):
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("Sale End Time")
    instructors = models.ManyToManyField(Instructor)
    

class Student(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    def __str__(self):
        return self.first_name + " " + self.last_name
