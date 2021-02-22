import pytest
import json

from mapper.serializers import IpAddressSerializer, GeoDataSerializer
from mapper.models import GeoData

pytestmark = pytest.mark.django_db



def test_ip_address_serializer():
    data = b"""{
    "ip":"154.121.11.143",
    "type":"ipv4",
    "continent_code":"EU",
    "continent_name":"Europe",
    "country_code":"PL",
    "country_name":"Poland",
    "region_code":"DS",
    "region_name":"Lower Silesia",
    "city":"Wroc\u0142aw",
    "zip":"50-124",
    "latitude":51.114891052246094,
    "longitude":17.038040161132812,
    "location":{
        "geoname_id":3081368,
        "capital":"Warsaw",
        "languages":[
        {
            "code":"pl",
            "name":"Polish",
            "native":"Polski"
        }
        ],
        "country_flag":"http:\/\/assets.ipstack.com\/flags\/pl.svg",
        "country_flag_emoji":"\ud83c\uddf5\ud83c\uddf1",
        "country_flag_emoji_unicode":"U+1F1F5 U+1F1F1",
        "calling_code":"48",
        "is_eu":true
    }
    }"""
    
    serialized_data = GeoDataSerializer.prepare_data(data)
    serialized_data = GeoDataSerializer(data=serialized_data)
    assert serialized_data.is_valid()
    obj = serialized_data.save()
    assert GeoData.objects.all().last() == obj

