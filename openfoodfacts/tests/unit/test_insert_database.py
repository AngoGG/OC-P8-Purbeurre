import pytest
from product.models import Category, Product
from tests.conftest import Config


@pytest.mark.django_db(transaction=True)
def test_insert_database():
    """ Method testing the insertion of a product into a database """
    results = Config.PRODUCT_RESULTS
    category = Category.objects.create(name="Boissons")
    Product.objects.create(**results)
    category.products.add(results["code"])
    assert Product.objects.count() == 1
    assert Category.objects.count() == 1
    assert len(category.products.all()) == 1
