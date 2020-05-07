# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-06 21:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('econapp', '0003_auto_20200507_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='login',
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
