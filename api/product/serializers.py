from rest_framework import serializers

from api.category.serializers import (CategoryProductSerializer,
                                      SubCategorySerializer)
from product.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    category = CategoryProductSerializer(source='sub_category.parent')

    class Meta:
        model = Product
        fields = (
            'name',
            'text',
            'slug',
            'price',
            'category',
            'sub_category',
            'image'
        )
