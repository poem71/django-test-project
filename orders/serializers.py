from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date', 'product_type', 'size', 'requester_name',
                  'quantity', 'manufacturer', 'unloading_place', 'description']