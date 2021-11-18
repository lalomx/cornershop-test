from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from lunch.models import Menu, Notification, Order
from lunch.serializers import MenuSerializer, NotificationSerializer, OrderSerializer
from lunch.tasks import SlackNotification


class NotificationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        serializer.save()
        data = serializer.data
        slack_notification = SlackNotification()
        slack_notification.apply_async(data["id"])


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
