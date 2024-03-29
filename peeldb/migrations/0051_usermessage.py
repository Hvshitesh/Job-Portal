# Generated by Django 3.2.4 on 2021-06-15 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0050_metadata"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=2000)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "job_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="peeldb.jobpost",
                    ),
                ),
                (
                    "message_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_messaged_from",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "message_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_message_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
