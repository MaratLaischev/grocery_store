from django.urls import include, path

urlpatterns = [
    path('', include('api.auth.urls')),
    path('', include('api.cart.urls')),
    path('', include('api.product.urls')),
    path('', include('api.category.urls')),
]
