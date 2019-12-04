# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-03 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econapp', '0019_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='econapp.Cart'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
