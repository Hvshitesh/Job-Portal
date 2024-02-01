# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0032_skill_skill_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("full-time", "Full Time"),
                    ("internship", "Internship"),
                    ("walk-in", "Walk-in"),
                    ("government", "Government"),
                    ("Fresher", "Fresher"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="searchresult",
            name="job_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("full-time", "Full Time"),
                    ("internship", "Internship"),
                    ("walk-in", "Walk-in"),
                    ("government", "Government"),
                    ("Fresher", "Fresher"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skill_type",
            field=models.CharField(
                choices=[("it", "IT"), ("non-it", "Non-IT"), ("other", "Other")],
                default="it",
                max_length=20,
            ),
        ),
    ]
