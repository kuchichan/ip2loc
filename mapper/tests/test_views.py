import pytest

from django.urls import reverse

from mapper.models import IpAddress
from mapper.views import MapperView
from .factories import geo_data 
pytestmark = pytest.mark.django_db

def test_get_geo_loc_from_ip_address(rf, geo_data):

    ip_address = IpAddress.objects.create(ip_address="192.168.0.1", geo_data=geo_data)
    url = reverse("mapper:map", kwargs={"ip_address": ip_address.ip_address})
    response = rf.get(url)
    print(response.status_code)
