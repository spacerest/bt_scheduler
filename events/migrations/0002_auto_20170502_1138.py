# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('content', models.CharField(max_length=20000)),
                ('timesent', models.DateTimeField(verbose_name='Sent time')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='class_size',
            field=models.PositiveSmallIntegerField(default=12),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(default='Class', max_length=30),
        ),
    ]
