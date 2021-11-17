from django.urls import include, path
from rest_framework.routers import SimpleRouter

from lunch.views import MenuViewSet, NotificationViewSet, OrderViewSet, index

router = SimpleRouter(trailing_slash=False)
router.register(r"menu", MenuViewSet)
router.register(r"order", OrderViewSet)
router.register(r"notification", NotificationViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
]
