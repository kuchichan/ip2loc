from rest_framework import viewsets

from mapper.models import IpAddress, GeoData
from mapper.serializers import  IpAddressSerializer, GeoDataSerializer


class IpAddressViewSet(viewsets.ModelViewSet):
    queryset = IpAddress.objects.all()
    serializer_class = IpAddressSerializer


class GeoDataViewSet(viewsets.ModelViewSet):
    queryset = IpAddress.objects.all()
    serializer_class = GeoDataSerializer
