# Generated by Django 2.0.2 on 2018-10-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0044_jobpost_pincode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="company_emails",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
