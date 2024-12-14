from django.db.models import F, Avg, Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from django.core.cache import cache

class ProductAnalyticsView(APIView):
    def get(self, request):
        cache_key = f"api:{request.GET.urlencode()}"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data)
        category = request.GET.get('category', '')
        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price', float('inf'))

        # Filtering
        if category:
            products = Product.objects.filter(
                category__iexact=category,
                price__gte=min_price,
                price__lte=max_price
            )
            # self.stdout.write(self.style.SUCCESS('Successfully imported data for Category'))
        else:
            products = Product.objects.filter(
                price__gte=min_price,
                price__lte=max_price
            )
            # self.stdout.write(self.style.SUCCESS('Successfully imported data for No Category'))
        # Aggregation
        stats = products.aggregate(
            total_products=Count('id'),
            average_price=Avg('price'),
            total_stock_value=Sum(F('stock') * F('price'))
        )
        response_data = {
            'total_products': stats['total_products'] or 0,
            'average_price': stats['average_price'] or 0.0,
            'total_stock_value': stats['total_stock_value'] or 0.0
        }
        cache.set(cache_key, stats, timeout=300) # Cache for 5 minutes
        return Response(response_data)
