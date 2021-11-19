from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter

from lunch.views import ChooseView, EmployeeViewSet, MenuViewSet, OrderViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r"menu", MenuViewSet)
router.register(r"order", OrderViewSet)
router.register(r"employee", EmployeeViewSet)

urlpatterns = [
    path("", login_required(TemplateView.as_view(template_name="index.html"))),
    path("choose/<uuid:id>", ChooseView.as_view(), name="choose"),
    path("thanks", TemplateView.as_view(template_name="thanks.html")),
    path("out", TemplateView.as_view(template_name="out.html")),
    path("api/", include(router.urls)),
]
