# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0015_auto_20170422_1154"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="published_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
