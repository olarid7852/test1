from django.urls import path, include
from rest_framework import routers
from .views import CarViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
]