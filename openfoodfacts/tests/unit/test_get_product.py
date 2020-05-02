import requests
from openfoodfacts.api import DataCleaner


def test_get_product() -> None:
    """ Method testing the generation of a product for database insertion """
    data = {
        "count": 9000,
        "page": "1",
        "page_size": "20",
        "products": [
            {
                "categories": "Boissons, Boissons gazeuses, Eaux, Eaux de sources, Eaux minérales, Boissons sans alcool, Eaux gazeuses, Eaux minérales naturelles, Eaux minérales gazeuses, Boissons sans sucre ajouté",
                "code": "3068320115160",
                "image_nutrition_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
                "image_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
                "nutriscore_grade": "a",
                "product_name": "La Salvetat",
                "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
            }
        ],
        "skip": 0,
    }

    results = {
        "code": "3068320115160",
        "name": "La Salvetat",
        "nutriscore_grade": "A",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
        "image": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutrient_levels": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
    }

    data_cleaner: DataCleaner = DataCleaner()
    for product in data_cleaner.get_product(data, "Boissons"):
        assert product == results
