import pytest


@pytest.fixture
def category():
    from category.models import Category
    return Category.objects.create(name='Тестовая категория', slug='slug')


@pytest.fixture
def sub_category(category):
    from category.models import SubCategory
    return SubCategory.objects.create(
        parent=category, name='Тестовая подкатегория', slug='slag'
    )


@pytest.fixture
def product(sub_category):
    from product.models import Product
    return Product.objects.create(
        sub_category=sub_category,
        name='Тестовый продукт',
        text='Тестовый продукт', price=123
    )


@pytest.fixture
def cart(product, user):
    from cart.models import Cart
    return Cart.objects.create(user=user, product=product, quantity=2)
