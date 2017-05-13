# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20170511_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='google_map_url',
            field=models.URLField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2972.783494517082!2d-87.65254728456031!3d41.83295997922574!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880e2c371b43fa8b%3A0x7d61c7fc22f0c3d9!2s942+W+34th+St%2C+Chicago%2C+IL+60608!5e0!3m2!1sen!2sus!4v1494542611669'),
        ),
    ]
