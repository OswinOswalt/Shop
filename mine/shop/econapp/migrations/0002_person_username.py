# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-06 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default=models.CharField(max_length=50), max_length=20),
        ),
    ]
