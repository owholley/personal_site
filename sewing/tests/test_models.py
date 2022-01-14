import pytest

# from ..models import Product, Image
from .factories import ProductFactory, ImageFactory

pytestmark = pytest.mark.django_db


def test_product__str__():
    product = ProductFactory()
    assert product.__str__() == product.name
    assert str(product) == product.name

def test_product_get_absolute_url():
    product = ProductFactory()
    url = product.get_absolute_url()
    assert url == f'/sewing/{product.slug}/'

def test_image__str__():
    image = ImageFactory()
    assert image.__str__() == image.name
    assert str(image) == image.name