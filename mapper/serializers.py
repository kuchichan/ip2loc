import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import IpAddress, GeoData


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = "__all__"


class GeoDataSerializer(serializers.ModelSerializer):
    zip = serializers.CharField(source="zip_code")

    class Meta:
        model = GeoData
        fields = (
            "continent_code",
            "continent_name",
            "country_code",
            "country_name",
            "region_code",
            "region_name",
            "city",
            "latitude",
            "longitude",
            "zip",
        )

    # Neeeded?
    @staticmethod
    def prepare_data(data: bytes) -> dict:
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        parsed_data.pop("ip")
        parsed_data.pop("location")
        parsed_data.pop("type")
        return parsed_data
