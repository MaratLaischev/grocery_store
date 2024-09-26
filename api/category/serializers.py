import base64
from django.core.files.base import ContentFile
from rest_framework import serializers

from category.models import Category, SubCategory


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        print(1111111)
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="photo." + ext)
        return super().to_internal_value(data)


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = (
            'name',
            'slug',
            'image'
        )


class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(source='sub_categori', many=True)
    image = Base64ImageField()

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image',
            'sub_category',
        )


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image',
        )
