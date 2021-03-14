from django.db import models


class GeoData(models.Model):
    continent_code = models.CharField(max_length=5)
    continent_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=5)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    geo_data = models.ForeignKey(
        GeoData, on_delete=models.CASCADE, related_name="ip_adresses"
    )
