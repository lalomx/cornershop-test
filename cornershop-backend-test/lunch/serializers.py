from rest_framework.serializers import DateField, ModelSerializer, UUIDField

from lunch.models import Employee, Menu, Order


class EmployeeSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Employee
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    id = UUIDField()
    date = DateField()

    class Meta:
        model = Menu
        fields = "__all__"


class CreateOrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializer(CreateOrderSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Order
        fields = "__all__"
