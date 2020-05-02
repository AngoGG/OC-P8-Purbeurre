import pytest
from product.models import Category, Product


@pytest.mark.django_db(transaction=True)
""" Method testing the insertion of a product into a database """
def test_insert_database():
    results = {
        "code": "3068320115160",
        "name": "La Salvetat",
        "nutriscore_grade": "A",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
        "image": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutrient_levels": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
    }
    category = Category.objects.create(name="Boissons")
    Product.objects.create(**results)
    category.products.add(results["code"])
    assert Product.objects.count() == 1
    assert Category.objects.count() == 1
    assert len(category.products.all()) == 1
