# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0024_auto_20170725_1747"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employmenthistory",
            name="from_date",
            field=models.DateField(null=True),
        ),
    ]
