# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-07 07:37
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('econapp', '0009_auto_20200507_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('login', models.CharField(default=False, max_length=30)),
                ('passw', models.CharField(default=False, max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='e_mail',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='econapp.User'),
        ),
    ]