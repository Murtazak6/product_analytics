from rest_framework import serializers
from .models import Product

class ProductAnalyticsSerializer(serializers.Serializer):
    total_products = serializers.IntegerField()
    average_price = serializers.FloatField()
    total_stock_value = serializers.FloatField()
