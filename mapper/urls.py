from django.urls import path
from rest_framework import routers

from mapper.views import IpAddressViewSet, GeoDataViewSet, MapperView

app_name = "mapper"

router = routers.DefaultRouter()
router.register(r"ip_adresses", IpAddressViewSet, basename="ip_adresses")
router.register(r"geo_data", GeoDataViewSet, basename="geo_data")

urlpatterns = [
    path("<str:ip_address>/", MapperView.as_view()),
]
