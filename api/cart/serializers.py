from rest_framework import serializers

from cart.models import Cart
from product.models import Product


class CartProductSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'quantity'
        )

    def get_quantity(self, obj):
        return self.context.get('quantity')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'quantity'
        )

    def to_representation(self, instance):
        context = {
            'request': self.context.get('request'),
            'quantity': instance.quantity
        }
        serializers = CartProductSerializer(instance.product, context=context)
        return serializers.data

    def validate(self, attrs):
        user = self.context.get('request').user
        method = self.context.get('request').method
        cart = Cart.objects.filter(user=user)
        if method == 'POST':
            if cart.filter(product=attrs['product']).exists():
                raise serializers.ValidationError(
                    'В карзине уже есть этот продукт'
                )
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('product'):
            validated_data.pop('product')
        return super().update(instance, validated_data)
