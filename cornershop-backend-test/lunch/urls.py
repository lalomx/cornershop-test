from django.urls import include, path
from rest_framework.routers import SimpleRouter

from lunch.views import MenuViewSet, index, send_notification

router = SimpleRouter(trailing_slash=False)
router.register(r"menu", MenuViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("notification/", send_notification, name="notification"),
    path("api/", include(router.urls)),
]
