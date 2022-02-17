# Generated by Django 4.0.2 on 2022-02-16 17:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0009_usersettings_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersettings",
            name="report_time",
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
