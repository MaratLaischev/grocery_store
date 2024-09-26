from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'text',
        'price',
        'sub_category',
        'image'
    )

    search_fields = ('id', 'name')
    list_filter = ('sub_category__parent', 'sub_category')


admin.site.register(Product, ProductAdmin)
