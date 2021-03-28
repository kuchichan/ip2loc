import pytest

from mapper.serializers import GeoDataSerializer
from mapper.models import GeoData

pytestmark = pytest.mark.django_db


def test_ip_address_serializer(json_data):

    serialized_data = GeoDataSerializer.prepare_data(json_data)
    serialized_data = GeoDataSerializer(data=serialized_data)
    assert serialized_data.is_valid()
    obj = serialized_data.save()
    assert GeoData.objects.all().last() == obj
