import uuid

from django.db import models


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("created_at", auto_now_add=True)
    updated = models.DateTimeField("created_at", auto_now_add=True)
    created_by = models.CharField(null=True, max_length=250)
    updated_by = models.CharField(null=True, max_length=250)

    class Meta:
        """Meta options"""

        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-updated"]


class Employee(CommonModel, models.Model):
    first_name = models.CharField(max_length=80, default="Unknown name")
    last_name = models.CharField(max_length=80, default="Unknown lastname")
    email = models.EmailField()


class Menu(CommonModel, models.Model):
    name = models.CharField(max_length=50, default="Unknown Menu")


class Dish(CommonModel, models.Model):
    name = models.CharField(max_length=50, default="Unknown Dish")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Order(CommonModel, models.Model):
    comments = models.TextField(null=True, max_length=500)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


class Notification(CommonModel, models.Model):
    channel_name = models.CharField(max_length=50, default="Unknown Channel")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
