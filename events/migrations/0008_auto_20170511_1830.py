# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20170511_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_url',
            new_name='abbreviation',
        ),
    ]