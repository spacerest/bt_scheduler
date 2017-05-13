# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-12 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20170512_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Class'),
        ),
    ]