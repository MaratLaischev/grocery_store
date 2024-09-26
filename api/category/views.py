from rest_framework.viewsets import ReadOnlyModelViewSet

from api.poginations import StandardResultsSetPagination
from category.models import Category

from .serializers import CategorySerializer


class CategoryView(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = StandardResultsSetPagination
