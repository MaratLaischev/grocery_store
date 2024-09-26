from django.db import models


class NameSlugImageModel(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Уникальный слаг', max_length=200, unique=True)
    image = models.ImageField(
        'Картинка', upload_to='category_img/', blank=True
    )

    class Meta:
        abstract = True
        ordering = ['name']


class Category(NameSlugImageModel):

    class Meta(NameSlugImageModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(NameSlugImageModel):
    parent = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_categori',
        verbose_name='Категория',
    )

    class Meta(NameSlugImageModel.Meta):
        verbose_name = 'подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
