from rest_framework.viewsets import ReadOnlyModelViewSet

from api.poginations import StandardResultsSetPagination
from product.models import Product

from .serializers import ProductsSerializer


class ProductView(ReadOnlyModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination
