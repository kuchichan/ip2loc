import pytest

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from mapper.models import GeoData, IpAddress
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


@pytest.fixture
def mocked_request(mocker, json_data_dict):
    mocked_json = mocker.MagicMock()
    mocked_json.json.return_value = json_data_dict

    mock = mocker.patch("requests.get", return_value=mocked_json)

    return mock


def test_get_geo_loc_from_ip_address(client_jwt, geo_data, ip_address):
    url = reverse("mapper:map", kwargs={"ip_address": ip_address.ip_address})
    response = client_jwt.get(url)
    assert response.status_code == 200
    assert GeoDataSerializer(geo_data).data == response.data


def test_build_url():
    ip_address = "192.168.0.1"
    mapper_view = MapperView()
    api_key = mapper_view.api_key_dict["access_key"]

    url = mapper_view.build_url(ip_address)

    assert url == mapper_view.ipstack_url + ip_address + "?" + f"access_key={api_key}"


def test_get_geodata_from_ip(mocked_request, json_data_dict):
    ip_address = "192.168.0.1"

    mapper_view = MapperView()
    result = mapper_view.get_geodata_from_ip(ip_address)
    mocked_request.assert_called_with(mapper_view.build_url(ip_address))

    assert result == json_data_dict


def test_post_mapper_view(mocked_request, json_data_dict, client_jwt):
    url = reverse("mapper:map", kwargs={"ip_address": "154.121.11.143"})
    response = client_jwt.post(url)
    ip_address_model = IpAddress.objects.last()

    assert response.status_code == 200
    assert ip_address_model.ip_address == "154.121.11.143"
    assert ip_address_model.geo_data.region_code == "DS"
    assert ip_address_model.geo_data.country_code == "PL"


def test_delete_mapper_view(client_jwt, geo_data):
    address = "192.255.10.12"
    IpAddress.objects.create(ip_address=address, geo_data=geo_data)

    url = reverse("mapper:map", kwargs={"ip_address": address})
    response = client_jwt.delete(url)

    assert response.status_code == 204
    with pytest.raises(GeoData.DoesNotExist):
        GeoData.objects.get(ip_adresses__ip_address=address)
