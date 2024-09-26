from django.urls import include, path
from rest_framework import routers

from .views import ProductView

product_v1 = routers.DefaultRouter()
product_v1.register(
    'products', ProductView, basename='products'
)

urlpatterns = [
    path('', include(product_v1.urls)),
]
