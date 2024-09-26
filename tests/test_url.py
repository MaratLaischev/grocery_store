from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, args',
    (
        ('products-list', None),
        ('products-detail', '1'),
        ('categories-list', None),
        ('categories-detail', '1'),
    )
)
def test_pages_availability_for_anonymous_user(client, product, name, args):
    url = reverse(name, args=args)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, args',
    (
        ('products-list', None),
        ('products-detail', '1'),
        ('cart-list', None),
        ('cart-detail', '1'),
    )
)
def test_pages_availability_for_auth_user(user_client, cart, name, args):
    url = reverse(name, args=args)
    response = user_client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_pages_availability_for_different_users(client, cart):
    url = reverse('cart-list')
    response = client.get(url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_new_cart(user_client, product):
    url = reverse('cart-list')
    data = {
        'product': 1,
        'quantity': 2
    }
    response = user_client.post(url, data=data)
    assert response.status_code == HTTPStatus.CREATED
