from rest_framework import routers
from mapper.views import IpAddressViewSet, GeoDataViewSet

router = routers.DefaultRouter()
router.register(r"ip_adresses", IpAddressViewSet, basename="ip_adresses")
router.register(r"geo_data", GeoDataViewSet, basename="geo_data")

