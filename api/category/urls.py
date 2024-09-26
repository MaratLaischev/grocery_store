from django.urls import include, path
from rest_framework import routers

from .views import CategoryView

categories_v1 = routers.DefaultRouter()
categories_v1.register(
    'categories', CategoryView, basename='categories'
)

urlpatterns = [
    path('', include(categories_v1.urls)),
]
