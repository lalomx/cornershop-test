from rest_framework.serializers import ModelSerializer, UUIDField

from lunch.models import Menu, Notification, Order


class NotificationSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Notification
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Menu
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Order
        fields = "__all__"
