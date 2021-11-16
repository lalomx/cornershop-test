from django.urls import path, include
from rest_framework.routers import SimpleRouter

from lunch.views import index, send_notification, MenuViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'menu', MenuViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('notification/', send_notification, name='notification'),
    path('api/', include(router.urls)),
    
]