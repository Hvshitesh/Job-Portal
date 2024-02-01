# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0036_auto_20171027_1518"),
    ]

    operations = [
        migrations.AddField(
            model_name="country",
            name="slug",
            field=models.SlugField(default="", max_length=500),
        ),
        migrations.AddField(
            model_name="state",
            name="slug",
            field=models.SlugField(default="", max_length=500),
        ),
    ]
