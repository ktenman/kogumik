# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 20:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20170214_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_commented',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 2, 14, 20, 8, 0, 443841, tzinfo=utc)),
        ),
    ]
