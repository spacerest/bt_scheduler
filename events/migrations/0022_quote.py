# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-22 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_auto_20180721_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000000)),
                ('author', models.CharField(max_length=1000)),
                ('source', models.URLField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
