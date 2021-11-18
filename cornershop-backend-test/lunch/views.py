from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from lunch.models import Menu, Order
from lunch.serializers import MenuSerializer, OrderSerializer
from lunch.tasks import SlackNotification


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

    @action(detail=False, url_path="week/(?P<week>[^/.]+)")
    def week(self, request, week=None, pk=None):
        menus = Menu.objects.filter(date__week=week)
        serializer = self.get_serializer(menus, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
        data = serializer.data
        slack_notification = SlackNotification()
        slack_notification.delay(str(data["id"]))


class OrderViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
