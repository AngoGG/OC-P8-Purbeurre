import pytest
import requests
from django.test import TestCase
from _pytest.monkeypatch import MonkeyPatch
from typing import Dict
from openfoodfacts.api import Api, DataCleaner
from product.models import Category, Product
from tests.conftest import Config


class TestApi:
    def test__product_is_valid(self) -> None:
        """ Method testing the generation of a product for database insertion """
        data_cleaner: DataCleaner = DataCleaner()
        assert data_cleaner._product_is_valid(Config.VALID_PRODUCT_DATA) == True
        assert data_cleaner._product_is_valid(Config.PRODUCT_DATA_EMPTY_FIELD) == False
        assert (
            data_cleaner._product_is_valid(Config.PRODUCT_DATA_MISSING_FIELD) == False
        )

    def test_get_product(self) -> None:
        """ Method testing the generation of a product for database insertion """
        results = Config.PRODUCT_RESULTS
        data_cleaner: DataCleaner = DataCleaner()
        for product in data_cleaner.get_product(Config.OPENFOODFACTS_DATA, "Boissons"):
            assert product == results

    @pytest.mark.django_db(transaction=True)
    def test_insert_database(self):
        """ Method testing the insertion of a product into a database """
        results = Config.PRODUCT_RESULTS
        category = Category.objects.create(name="Boissons")
        Product.objects.create(**results)
        category.products.add(results["code"])

        assert Product.objects.count() == 1
        product_data = Product.objects.first()
        for attr_key, attr_val in results.items():
            assert results[attr_key] == getattr(product_data, attr_key)

        assert Category.objects.count() == 1
        assert Category.objects.first().name == "Boissons"
        assert len(category.products.all()) == 1

    def test_get_data(self, monkeypatch: MonkeyPatch) -> None:
        """ Method testing data recovery via the OpenFoodFacts API """

        class MockResponse:
            # mock json() method always returns a specific testing dictionary
            @staticmethod
            def json() -> Dict:
                return Config.OPENFOODFACTS_DATA

        api: Api = Api()

        def mockreturn(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr(requests, "get", mockreturn)
        assert api.get_data("Boissons") == Config.OPENFOODFACTS_DATA
