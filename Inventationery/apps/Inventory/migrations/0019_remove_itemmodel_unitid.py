# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 00:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0018_auto_20151227_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmodel',
            name='UnitId',
        ),
    ]
