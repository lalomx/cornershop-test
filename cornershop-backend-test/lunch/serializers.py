from rest_framework.serializers import ModelSerializer

from lunch.models import Menu, Order


class MenuSerializerSlim(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name"]


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    menu = MenuSerializerSlim()

    class Meta:
        model = Order
        fields = "__all__"
