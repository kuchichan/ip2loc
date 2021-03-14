from mapper.tests.factories import geo_data
import requests
from urllib import parse
from django.conf import settings
from django.http import Http404

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

    def get_address(self, ip_address):
        try:
            return IpAddress.objects.get(ip_address=ip_address)
        except IpAddress.DoesNotExist:
            raise Http404

    def build_url(self, ip_address):
        url = self.ipstack_url + ip_address + "?"
        return url + parse.urlencode(self.api_key_dict)

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
            return Response(status=status.HTTP_400_BAD_REQUEST)

        IpAddress.objects.create(ip_address=ip_address, geo_data=geo_data)

        return Response(status=status.HTTP_200_OK)

    def get(self, request, ip_address):
        ip_address = self.get_address(ip_address)
        serializer = GeoDataSerializer(ip_address.geo_data)
        return Response(serializer.data)

    def put(self, request, ip_address):
        ip_address = self.get_address(ip_address)
        serializer = GeoDataSerializer(ip_address.geo_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, ip_address):
        ip_address = self.get_address(ip_address)
        serializer = GeoDataSerializer(
            ip_address.geo_data, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ip_address):
        geo_data = GeoData.objects.filter(ip_adresses__ip_address=ip_address)
        geo_data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
