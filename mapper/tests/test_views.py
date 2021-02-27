import pytest

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from mapper.models import IpAddress
from mapper.serializers import GeoDataSerializer
from mapper.views import MapperView

from .factories import geo_data

pytestmark = pytest.mark.django_db


@pytest.fixture
def client_jwt(django_user_model):
    name = "Me"
    pwd = "hello"
    user = django_user_model.objects.create_user(username=name, password=pwd)
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client


@pytest.fixture
def ip_address(geo_data):
    ip_address = IpAddress.objects.create(ip_address="192.168.0.1", geo_data=geo_data)
    return ip_address


def test_get_geo_loc_from_ip_address(client_jwt, geo_data, ip_address):
    url = reverse("mapper:map", kwargs={"ip_address": ip_address.ip_address})
    response = client_jwt.get(url)
    assert response.status_code == 200
    assert GeoDataSerializer(geo_data).data == response.data
