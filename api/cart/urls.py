from django.urls import include, path
from rest_framework import routers

from .views import CartView

cart_v1 = routers.DefaultRouter()
cart_v1.register(
    'cart', CartView, basename="cart"
)

urlpatterns = [
    path('', include(cart_v1.urls)),
]
