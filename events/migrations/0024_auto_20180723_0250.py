# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-23 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form',
            new_name='Document',
        ),
    ]
