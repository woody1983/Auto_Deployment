# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoDeployment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='AutoDeployment',
        ),
    ]
