# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0029_auto_20170830_1702"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agencyresume",
            name="experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
