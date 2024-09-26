from django.db import models
from category.models import SubCategory


class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Описание')
    slug = models.SlugField('Уникальный слаг', max_length=200, unique=True)
    price = models.PositiveSmallIntegerField('Цена')
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория'
    )
    image = models.ImageField('Картинка', upload_to='recipe_img/', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
