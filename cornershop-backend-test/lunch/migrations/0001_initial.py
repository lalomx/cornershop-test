# Generated by Django 3.0.8 on 2021-11-16 03:07
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                ("created_by", models.CharField(max_length=250, null=True)),
                ("updated_by", models.CharField(max_length=250, null=True)),
                ("name", models.CharField(default="Unknown Dish", max_length=50)),
            ],
            options={
                "ordering": ["-created", "-updated"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                ("created_by", models.CharField(max_length=250, null=True)),
                ("updated_by", models.CharField(max_length=250, null=True)),
                ("first_name", models.CharField(default="Unknown name", max_length=80)),
                (
                    "last_name",
                    models.CharField(default="Unknown lastname", max_length=80),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "ordering": ["-created", "-updated"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                ("created_by", models.CharField(max_length=250, null=True)),
                ("updated_by", models.CharField(max_length=250, null=True)),
                ("name", models.CharField(default="Unknown Menu", max_length=50)),
            ],
            options={
                "ordering": ["-created", "-updated"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                ("created_by", models.CharField(max_length=250, null=True)),
                ("updated_by", models.CharField(max_length=250, null=True)),
                ("comments", models.TextField(max_length=500, null=True)),
                (
                    "dish",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lunch.Dish",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lunch.Employee",
                    ),
                ),
            ],
            options={
                "ordering": ["-created", "-updated"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                ("created_by", models.CharField(max_length=250, null=True)),
                ("updated_by", models.CharField(max_length=250, null=True)),
                (
                    "channel_name",
                    models.CharField(default="Unknown Channel", max_length=50),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lunch.Employee",
                    ),
                ),
            ],
            options={
                "ordering": ["-created", "-updated"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="dish",
            name="menu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="lunch.Menu"
            ),
        ),
    ]
