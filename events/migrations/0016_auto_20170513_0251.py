# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 02:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_class_abbreviation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='class_name',
            new_name='name',
        ),
    ]
