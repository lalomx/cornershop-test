# Generated by Django 3.0.8 on 2021-11-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lunch", "0004_notification_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="slack_id",
            field=models.CharField(default="00000", max_length=25),
        ),
    ]
