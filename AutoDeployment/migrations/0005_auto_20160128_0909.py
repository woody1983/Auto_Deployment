# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoDeployment', '0004_auto_20160128_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RFC_Number', models.CharField(max_length=50)),
                ('RFC_STATUS', models.CharField(choices=[('p', 'Pending'), ('r', 'Processing'), ('f', 'Failed'), ('a', 'Approved'), ('d', 'Canceled'), ('c', 'Completed')], default='p', max_length=1)),
                ('Entry_Time', models.DateTimeField(auto_now_add=True, verbose_name='Entry Time')),
                ('Modify_Time', models.DateTimeField(auto_now=True, verbose_name='Modify Time')),
                ('Deploy_Date', models.DateTimeField(null=True, verbose_name='Deploy Date')),
                ('Deploy_Server', models.CharField(choices=[('d', 'Deploy_Test'), ('i', 'INT_SHA')], default='d', max_length=1)),
                ('Completed_Time', models.DateTimeField(null=True, verbose_name='Deploy Date')),
                ('Deploy_Log', models.CharField(max_length=1000)),
                ('Change_Type', models.CharField(choices=[('t', 'New Table'), ('c', 'New Column'), ('u', 'Change Data'), ('s', 'SP FUNC'), ('i', 'Insert Data'), ('a', 'Alter Table')], default='', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='AutoDeployment',
        ),
    ]
