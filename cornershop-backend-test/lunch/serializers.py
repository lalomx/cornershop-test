from rest_framework.serializers import ModelSerializer

from lunch.models import Menu, Order


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
