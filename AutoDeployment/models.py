from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

MAYBECHOICE = (
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('failed', 'Failed'),
    ('approved', 'Approved'),
    ('canceled', 'Canceled'),
    ('completed', 'Completed'),
)

DEPLOYSERVER = (
    ('deploy_server', 'Deploy_Test'),
    ('int_sha', 'INT_SHA'),
)

CHANGE_TYPE = (
    ('t', 'New Table'),
    ('c', 'New Column'),
    ('u', 'Change Data'),
    ('s', 'SP FUNC'),
    ('i', 'Insert Data'),
    ('a', 'Alter Table'),
)

# 'Pending','Processing','Failed','Approved','Canceled','Completed'
#`Deploy_Server` enum('SHA_PIXOS2','SZX_PIXOS2','NGB_PIXOS2','HKG_PIXOS2','TPE_PIXOS2','BOM_PIXOS2','CenterServer','ShareData5','CAS','INT_SHA','INT_NGB','Deploy_Test') DEFAULT 'Deploy_Test',
# `Change_Type` enum('New Table','New Column','Change Data','SP','Insert Data','Alter Table') DEFAULT NULL,
# Create your models here.
class Deploy(models.Model):
    RFC_Number = models.CharField(max_length=50)
    RFC_SQL = models.TextField(max_length=50000)
    RFC_STATUS = models.CharField(max_length=20, choices=MAYBECHOICE, default='pending')
    Entry_Time = models.DateTimeField('Entry Time',auto_now_add = True)
    Modify_Time = models.DateTimeField('Modify Time', auto_now = True)
    Deploy_Date = models.DateTimeField('Deploy Date', null = True)
    Deploy_Server = models.CharField(max_length=20, choices=DEPLOYSERVER, default='deploy_server')
    Completed_Time = models.DateTimeField('Deploy Date', null = True)
    Deploy_Log = models.CharField(max_length=1000, null=True)
    Change_Type = models.CharField(max_length=1, choices=CHANGE_TYPE, default='')

