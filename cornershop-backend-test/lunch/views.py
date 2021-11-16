from django.http import HttpResponse
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from lunch.models import Menu
from lunch.serializers import MenuSerializer
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
    lookup_value_regex = "[0-9a-f]{32}"
    lookup_field = "id"

    @action(detail=True)
    def orders(self, request, pk=None):
        pass
