import pytest


@pytest.fixture
def json_data():
    return b"""{
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


@pytest.fixture
def json_data_dict():
    return {
        "ip": "154.121.11.143",
        "type": "ipv4",
        "continent_code": "EU",
        "continent_name": "Europe",
        "country_code": "PL",
        "country_name": "Poland",
        "region_code": "DS",
        "region_name": "Lower Silesia",
        "city": "Wroc\u0142aw",
        "zip": "50-124",
        "latitude": 51.114891052246094,
        "longitude": 17.038040161132812,
        "location": {
            "geoname_id": 3081368,
            "capital": "Warsaw",
            "languages": [{"code": "pl", "name": "Polish", "native": "Polski"}],
            "country_flag": "http:\/\/assets.ipstack.com\/flags\/pl.svg",
            "country_flag_emoji": "\ud83c\uddf5\ud83c\uddf1",
            "country_flag_emoji_unicode": "U+1F1F5 U+1F1F1",
            "calling_code": "48",
            "is_eu": True,
        },
    }
