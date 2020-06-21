import pytest
from django.test import TestCase
from product.models import Product, Category
from tests.conftest import Config


@pytest.mark.django_db(transaction=True)
class TestProducts(TestCase):
    def test___str__(self):
        results = Config.PRODUCT_RESULTS
        Product.objects.create(**results)
        product = Product.objects.first()

        self.assertEqual(str(product), product.name)


@pytest.mark.django_db(transaction=True)
class TestCategory(TestCase):
    def test___str__(self):
        results = Config.PRODUCT_RESULTS
        category = Category.objects.create(name="Boissons")
        Product.objects.create(**results)

        self.assertEqual(str(category), category.name)
