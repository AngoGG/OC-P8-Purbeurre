#!/usr/bin/env python3

from typing import List, Dict, Any, Generator
import requests


class Api:
    """ Manages interactions with OpenFoodFact API """

    def __init__(self):
        self.base_url: str = "https://world.openfoodfacts.org/cgi/search.pl"
        self.payloads: Dict = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "Boissons",
            "sort_by": "unique_scans_n",
            "countries": "France",
            "purchase_places": "France",
            "page": 1,
            "page_size": 50,
            "json": 1,
        }

    def request(self) -> Dict:
        """ Get data from API, return json with results """
        response = requests.get(self.base_url, params=self.payloads)
        return response.json()

    def get_data(self, category: str) -> Dict:
        """ Gets data from the given category and returns it"""
        self.payloads["tag_0"] = category
        return self.request()


class DataCleaner:
    """ Manages the sorting and verification of data retrieved from the API before integration. """

    def __init__(self) -> None:
        """Constructor"""
        self.product_items_list: List[str, str] = [
            "nutriscore_grade",
            "product_name",
            "code",
            "categories",
            "url",
            "image_url",
            "image_nutrition_url",
        ]
        self.product_nutrients_list: List[str, str] = [
            "carbohydrates_100g",
            "sugars_100g",
            "fat_100g",
            "saturated-fat_100g",
            "proteins_100g",
            "salt_100g",
            "energy-kcal_100g",
        ]

    def get_product(self, datas: Dict[str, Any], category: str) -> Generator:
        """ Sorts the data to keep only what is needed in the database """
        for data in datas["products"]:
            if self._product_is_valid(data):
                if self._nutrients_are_valid(data["nutriments"]):
                    product: Dict = {
                        "code": data["code"],
                        "name": data["product_name"],
                        "nutriscore_grade": data["nutriscore_grade"],
                        "url": data["url"],
                        "image": data["image_url"],
                        "nutrient_levels": data["image_nutrition_url"],
                        "carbohydrates_100g": data["nutriments"]["carbohydrates_100g"],
                        "sugars_100g": data["nutriments"]["sugars_100g"],
                        "fat_100g": data["nutriments"]["fat_100g"],
                        "saturated_fat_100g": data["nutriments"]["saturated-fat_100g"],
                        "proteins_100g": data["nutriments"]["proteins_100g"],
                        "salt_100g": data["nutriments"]["salt_100g"],
                        "kcal_100g": data["nutriments"]["energy-kcal_100g"],
                    }
                    yield product

    def _product_is_valid(self, product: Dict[str, Any]) -> bool:
        """ Verifies the presence of all the elements required for a product
        and if the stores_tags list is not empty """
        for field in self.product_items_list:
            if field not in product:
                return False
            elif len(product[field]) == 0:
                return False
        return True

    def _nutrients_are_valid(self, product: Dict[str, str]) -> bool:
        """ Verifies the presence of all the elements required for a product
        and if the stores_tags list is not empty """
        for field in self.product_nutrients_list:
            if field not in product:
                return False
        return True
