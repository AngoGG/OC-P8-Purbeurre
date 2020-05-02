import requests
from openfoodfacts.api import Api


def test_get_data(monkeypatch) -> None:
    """ Method testing data recovery via the OpenFoodFacts API """
    results = {
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

    api: Api = Api()

    def mockreturn(self):
        return results

    monkeypatch.setattr(Api, "request", mockreturn)
    assert api.get_data("Boissons") == results
