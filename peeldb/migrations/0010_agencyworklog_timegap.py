# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-14 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0009_agencyworklog"),
    ]

    operations = [
        migrations.AddField(
            model_name="agencyworklog",
            name="timegap",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
