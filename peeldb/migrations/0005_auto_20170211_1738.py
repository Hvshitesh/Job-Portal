# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-11 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0004_auto_20170211_1724"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": (
                    ("support_view", "can view tickets"),
                    ("support_edit", "can edit tickets"),
                    ("activity_view", "can view recruiters, applicants, data, posts"),
                    ("activity_edit", "can edit data"),
                    ("jobposts_edit", "can create/edit/copy/delete jobposts"),
                    ("jobposts_invoice_access", "can edit/access the invoice"),
                    ("jobposts_resume_profiles", "can access agency resume profiles"),
                )
            },
        ),
    ]
