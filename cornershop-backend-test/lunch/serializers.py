from rest_framework.serializers import DateField, ModelSerializer, UUIDField

from lunch.models import Menu, Order


class MenuSerializer(ModelSerializer):
    id = UUIDField()
    date = DateField()

    class Meta:
        model = Menu
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Order
        fields = "__all__"
