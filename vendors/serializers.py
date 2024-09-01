from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance
import json

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = serializers.JSONField()
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
    
    def to_internal_value(self, data):
        if 'items' in data and isinstance(data['items'], str):
            try:
                data['items'] = json.loads(data['items'])
            except json.JSONDecodeError:
                raise serializers.ValidationError({'items': 'Must be valid JSON'})
        return super().to_internal_value(data)

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
