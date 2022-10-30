# serializers.py
from rest_framework import serializers

from .models import DeviceModel
from .models import Brand, DeviceType


class DeviceModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceModel
        fields = 'name'


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):

    # type = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    type = DeviceTypeSerializer(many=True)
    # type_id = serializers.PrimaryKeyRelatedField(queryset=DeviceType.objects.all(), write_only=True)

    class Meta:
        model = Brand
        fields = ("id", "name", "type")


class DeviceSerializer(serializers.ModelSerializer):

    # brand = BrandSerializer(read_only=True, many=True)
    # brands = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = DeviceType
        fields = "__all__"

