# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime
import calendar

class Class(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=3000, null=True, blank=True)
    abbreviation = models.CharField(max_length=20, default="error")
    def __str__(self):
        return self.name
    #def __str__(self):
    #    return self.class_name

class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    def __str__(self):
	return self.first_name + " " + self.last_name

class Location(models.Model):
    location_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    abbreviation = models.CharField(max_length=20, default="error")
    def __str__(self):
        return self.location_name
    google_map_url = models.URLField(max_length=600,default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2972.783494517082!2d-87.65254728456031!3d41.83295997922574!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880e2c371b43fa8b%3A0x7d61c7fc22f0c3d9!2s942+W+34th+St%2C+Chicago%2C+IL+60608!5e0!3m2!1sen!2sus!4v1494542611669")
    #def __str__(self):
	#return self.location_name
 
class Event(models.Model):
    class_type = models.ForeignKey(Class, models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("Sale End Time")
    instructors = models.ManyToManyField(Instructor)
    class_size = models.PositiveSmallIntegerField(default=12)
    location = models.ForeignKey(Location, models.SET_NULL, null=True, blank=True)
    def __str__(self):
	return "{}, {}, {}".format(self.class_type, self.location, self.start_time)

class Student(models.Model):
    first_name = models.CharField(max_length=30, default="Add last name")
    last_name = models.CharField(max_length=30, default="Add last name")
    birthday = models.DateField("Birthday",default=datetime.now)
    def __str__(self):
        return first_name + " " + last_name
    

       

#class Student(models.Model):
#
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=40)
#    birthday = models.DateField()
#    def __str__(self):
#        return self.first_name + " " + self.last_name

#for mail only

class Message(models.Model):
    subject = models.CharField(max_length=30)
    email = models.CharField(max_length=50,blank=True)
    content = models.CharField(max_length=20000)
    timesent = models.DateTimeField("Sent time")
    def __str__(self):
        return self.subject
