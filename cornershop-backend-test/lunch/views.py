from django.http import HttpResponse
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from lunch.models import Menu, Order
from lunch.serializers import MenuSerializer, OrderSerializer
from lunch.tasks import SlackNotification


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def send_notification(request, menu_id):
    notification = SlackNotification()
    notification.apply_async(menu_id)


class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = "id"

    @action(detail=True)
    def orders(self, request, id=None):
        orders = Order.objects.filter(menu=id)
        order_serializer = OrderSerializer(orders, many=True)

        return Response(order_serializer.data)


class OrderViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
