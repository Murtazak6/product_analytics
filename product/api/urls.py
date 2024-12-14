from django.urls import path
from .views import ProductAnalyticsView

urlpatterns = [
    path('products/analytics/', ProductAnalyticsView.as_view(), name='product-analytics'),
]
