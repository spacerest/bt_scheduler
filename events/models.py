# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime
import calendar

class Document(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=3000, null=True, blank=True)
    file = models.FileField(upload_to="", blank=True, null=True)
    def __str__(self):
        return self.title

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
    meeting_time_description = models.TextField(max_length=10000, null=True, blank=True)
    show_this_event = models.BooleanField(default=True)
    location = models.ForeignKey(Location, models.SET_NULL, null=True, blank=True)
    class_type = models.ForeignKey(Class, models.SET_NULL, null=True, blank=True)
    instructors = models.ManyToManyField(Instructor)
    def __str__(self):
	return "{}, {}".format(self.class_type, self.location )

class Student(models.Model):
    first_name = models.CharField(max_length=30, default="Add last name")
    last_name = models.CharField(max_length=30, default="Add last name")
    birthday = models.DateField("Birthday",default=datetime.now)
    def __str__(self):
        return first_name + " " + last_name
 
class Announcement(models.Model):
    text = models.CharField(max_length=100, default="insert announcement here")
    start_time = models.DateField("Start Day")
    end_time = models.DateField("End Day")
    show_start_end_times = models.BooleanField(default=True)
    show_outside_of_set_times = models.BooleanField(default=False)
    def __str__(self):
        return self.text   
    @property
    def started(self):
        return date.today() >= self.start_time
    @property
    def ended(self):
        return date.today() > self.end_time
    @property
    def today(self):
        return date.today()
    def is_multiple_days(self):
        if (self.start_time == self.end_time):
            return False 
        else:
            return True 

class Quote(models.Model):
    text = models.TextField(max_length=1000000)
    author = models.CharField(max_length=1000)
    source = models.URLField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return self.text


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
