# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-14 18:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0010_agencyworklog_timegap"),
    ]

    operations = [
        migrations.AddField(
            model_name="appliedjobs",
            name="resume_applicant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="peeldb.AgencyResume",
            ),
        ),
        migrations.AlterField(
            model_name="agencyapplicants",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Shortlisted", "Shortlisted"),
                    ("Selected", "Selected"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="appliedjobs",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
