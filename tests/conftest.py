from typing import List, Dict


class Config:

    OPENFOODFACTS_DATA = {
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

    PRODUCT_RESULTS = {
        "code": "3068320115160",
        "name": "La Salvetat",
        "nutriscore_grade": "a",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
        "image": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutrient_levels": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
    }
