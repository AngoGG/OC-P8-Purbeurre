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

    def test_get_substitute(self) -> None:
        product_code = "3068320115161"
        expected_code_substitute = "3068320115161"
        category = Category.objects.create(name="Boissons")
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)
            category.products.add(product["code"])
        substitute = Product.get_substitute(product_code, product["nutriscore_grade"])
        assert substitute[0].code == expected_code_substitute

    def test_get_category(self) -> None:
        category = Category.objects.create(name="Boissons")
        Product.objects.create(**Config.PRODUCT_RESULTS)
        category.products.add(Config.PRODUCT_RESULTS["code"])
        category = Product.get_category(Config.PRODUCT_RESULTS["code"])
        assert category[0].name == "Boissons"


@pytest.mark.django_db(transaction=True)
class TestCategory(TestCase):
    def test___str__(self):
        results = Config.PRODUCT_RESULTS
        category = Category.objects.create(name="Boissons")
        Product.objects.create(**results)

        self.assertEqual(str(category), category.name)
