# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0025_auto_20170801_1402"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="minified_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
