# Generated by Django 3.2.4 on 2021-06-15 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0051_usermessage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermessage",
            old_name="job_id",
            new_name="job",
        ),
    ]
