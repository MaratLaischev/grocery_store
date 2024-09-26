from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthorAndOwnerPermission
from cart.models import Cart

from .serializers import CartSerializer


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthorAndOwnerPermission,]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_grand_total_and_total_items(
        self, products: list
    ) -> tuple[int, int]:
        '''
        Получает список продуктов и выводит общюю цену и количество позиций
        '''
        full_price = 0
        total_items = 0
        for product in products:
            full_price += product['price'] * product['quantity']
            total_items += product['quantity']
        return full_price, total_items

    def list(self, request, *args, **kwargs):
        serializer = CartSerializer(self.get_queryset(), many=True)
        grand_total, total_items = self.get_grand_total_and_total_items(
            serializer.data
        )
        result = {
            'products': serializer.data,
            'total_items': total_items,
            'grand_total': grand_total
        }
        return Response(result, status=HTTP_200_OK)

    @action(
        detail=False,
        methods=['DELETE'],
    )
    def clear_cart(self, request):
        obj = self.get_queryset()
        if obj.exists():
            obj.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(
            {'error': 'Корзина пустая'},
            status=HTTP_400_BAD_REQUEST
        )
