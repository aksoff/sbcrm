from rest_framework import serializers

from .models import Brand, DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceType
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):

    # type = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    type = DeviceTypeSerializer(read_only=True, many=True)
    type_id = serializers.PrimaryKeyRelatedField(queryset=DeviceType.objects.all(), write_only=True)

    class Meta:
        model = Brand
        fields = ("name", "type_id", "type")

