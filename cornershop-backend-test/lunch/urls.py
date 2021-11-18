from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter

from lunch.views import MenuViewSet, OrderViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r"menu", MenuViewSet)
router.register(r"order", OrderViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("/<slug:slug>", TemplateView.as_view(template_name="index.html")),
    path("api/", include(router.urls)),
]
