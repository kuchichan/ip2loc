import requests
import urllib

from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from mapper.models import IpAddress, GeoData
from mapper.serializers import IpAddressSerializer, GeoDataSerializer


class IpAddressViewSet(viewsets.ModelViewSet):
    queryset = IpAddress.objects.all()
    serializer_class = IpAddressSerializer


class GeoDataViewSet(viewsets.ModelViewSet):
    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer


class MapperView(APIView):
    ipstack_url = "http://api.ipstack.com/"
    api_key_dict = dict(access_key=settings.API_KEY)
    permission_classes = [IsAuthenticated]

    def build_url(self, ip_address):
        url = self.ipstack_url + ip_address + "?"
        return url + urllib.parse.urlencode(self.api_key_dict)

    def get_geodata_from_ip(self, ip_address):
        url = self.build_url(ip_address)
        data = requests.get(url)
        return data.json()

    def post(self, request, ip_address):
        data = self.get_geodata_from_ip(ip_address)
        geo_data_serializer = GeoDataSerializer(data=data)

        if geo_data_serializer.is_valid():
            geo_data = geo_data_serializer.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        IpAddress.objects.create(ip_address=ip_address, geo_data=geo_data)

        return Response(status=status.HTTP_200_OK)
