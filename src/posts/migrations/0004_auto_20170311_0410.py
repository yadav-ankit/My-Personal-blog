# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 11, 4, 10, 34, 528830, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
