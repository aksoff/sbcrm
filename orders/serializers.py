# serializers.py
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    device_model = serializers.StringRelatedField(many=False)
    #status = serializers.IntegerField(choices=Order.ORDER_STATUS)

    class Meta:
        model = Order
        fields = ('id', 'order_date', 'customer', 'status', 'device_model', 'defect')
