# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170502_1138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='event',
            name='instructors',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]
