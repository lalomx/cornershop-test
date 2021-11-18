from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pytz import timezone

from lunch.forms import OrderForm
from lunch.models import Menu, Notification, Order
from lunch.serializers import CreateOrderSerializer, MenuSerializer, OrderSerializer
from lunch.tasks import SlackNotification


class ChooseView(FormView):
    template_name = "choose.html"
    form_class = OrderForm
    success_url = "/lunch/thanks"

    def form_valid(self, form, notification_id):
        form.create_order(notification_id)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        notification_id = str(kwargs["id"])
        notification = Notification.objects.get(id=notification_id)

        if notification.status == "D":
            return render(request, "thanks.html", {"done": True})

        form = self.get_form_with_choices(request.POST, notification)
        if form.is_valid():
            return self.form_valid(form, notification)
        else:
            return self.form_invalid(form)

    def get(self, request, id):
        clt = timezone("America/Santiago")
        date = datetime.now().astimezone(clt)

        if date.time().hour >= 11:
            return HttpResponseRedirect("/lunch/out")

        notification = Notification.objects.get(id=id)
        form = self.get_form_with_choices(None, notification)
        return render(request, self.template_name, {"form": form, "id": id})

    def get_form_with_choices(self, data, notification):
        menu = notification.menu
        form = self.form_class(data)
        form.fields["option"].choices = [
            (menu.option_one, menu.option_one),
            (menu.option_two, menu.option_two),
            (menu.option_three, menu.option_three),
            (menu.option_four, menu.option_four),
        ]

        return form


class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    generics.UpdateAPIView,
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

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderSerializer
        else:
            return self.serializer_class
