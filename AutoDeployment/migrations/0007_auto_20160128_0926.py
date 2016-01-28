# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoDeployment', '0006_auto_20160128_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='RFC_SQL',
            field=models.TextField(default='', max_length=50000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deploy',
            name='Modify_Time',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modify Time'),
        ),
    ]
