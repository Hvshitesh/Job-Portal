# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0036_auto_20171027_1518"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_register_through_mail",
        ),
    ]
