from django.core.validators import MinValueValidator
from django.db import models

from product.models import Product
from userauth.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cart'
    )
    quantity = models.PositiveSmallIntegerField(
        'Количество',
        validators=(MinValueValidator(
            1, message='Минимальное количество продуктов 1'),
        )
    )

    class Meta:
        ordering = ['user']
        verbose_name = 'карзина'
        verbose_name_plural = 'Карзины'

    def __str__(self):
        return self.user.username
