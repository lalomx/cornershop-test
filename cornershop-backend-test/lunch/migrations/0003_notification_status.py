# Generated by Django 3.0.8 on 2021-11-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0002_auto_20211116_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.CharField(default='P', max_length=1),
        ),
    ]
