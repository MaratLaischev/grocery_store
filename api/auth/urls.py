from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers

user_router_v1 = routers.DefaultRouter()
user_router_v1.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('user/', include('djoser.urls.authtoken')),
    path('user/', UserViewSet.as_view({'post': 'create'})),
    path('user/me/', UserViewSet.as_view({'get': 'me'})),
]
