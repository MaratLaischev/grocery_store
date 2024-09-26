from django.contrib import admin

from cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'quantity',
        'price'
    )

    search_fields = ('id', 'user__username', 'product__slug')
    list_filter = ('product__slug',)

    def price(self, obj):
        return obj.product.price * obj.quantity


admin.site.register(Cart, CartAdmin)
