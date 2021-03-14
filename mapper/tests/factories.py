import pytest
import factory
import factory.fuzzy

from mapper.models import GeoData


class GeoDataFactory(factory.django.DjangoModelFactory):
    continent_code = factory.Faker("country_code")
    continent_name = factory.Faker("name")
    country_code = factory.fuzzy.FuzzyText()
    country_name = factory.fuzzy.FuzzyText()
    region_code = factory.fuzzy.FuzzyText()
    region_name = factory.fuzzy.FuzzyText()
    city = factory.fuzzy.FuzzyText()
    zip_code = factory.fuzzy.FuzzyText()
    latitude = factory.fuzzy.FuzzyFloat(low=-90, high=90)
    longitude = factory.fuzzy.FuzzyFloat(low=-90, high=90)

    class Meta:
        model = GeoData


@pytest.fixture
def geo_data():
    return GeoDataFactory()
