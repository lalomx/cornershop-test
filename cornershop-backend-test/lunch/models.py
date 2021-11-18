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
    slack_id = models.CharField(max_length=25, null=False, blank=False, default="00000")


class Menu(CommonModel, models.Model):
    name = models.CharField(max_length=50, default="Unknown Menu")
    date = models.DateField(null=False, unique=True)
    option_one = models.CharField(max_length=250, default="Dish 1")
    option_two = models.CharField(max_length=250, default="Dish 2")
    option_three = models.CharField(max_length=250, default="Dish 3")
    option_four = models.CharField(max_length=250, default="Dish 4")


class Order(CommonModel, models.Model):
    comments = models.TextField(null=True, max_length=500)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    selection = models.CharField(max_length=50, default="No selection")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


class Notification(CommonModel, models.Model):
    channel_name = models.CharField(max_length=50, default="Unknown Channel")
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, default="NOT_SENT")
