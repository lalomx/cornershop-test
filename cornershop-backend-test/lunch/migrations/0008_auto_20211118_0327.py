# Generated by Django 3.0.8 on 2021-11-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lunch", "0007_menu_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="date",
            field=models.DateField(auto_now_add=True, unique=True),
        ),
    ]
