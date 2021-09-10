from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from devices.models import Brand
from devices.serialisers import BrandSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']

    def perform_create(self, serializer):
        # type = serializer.pop('type_id')
        serializer.save()
