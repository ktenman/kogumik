# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 20:06
from __future__ import unicode_literals

import django.utils.datetime_safe
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170214_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_commented',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
    ]
