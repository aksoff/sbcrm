from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from devices.models import Brand, DeviceType
from devices.serialisers import BrandSerializer, DeviceSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class DeviceViewSet(viewsets.ViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceSerializer
