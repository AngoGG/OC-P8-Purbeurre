import requests
from openfoodfacts.api import DataCleaner
from tests.conftest import Config


def test_get_product() -> None:
    """ Method testing the generation of a product for database insertion """
    results = Config.PRODUCT_RESULTS
    data_cleaner: DataCleaner = DataCleaner()
    for product in data_cleaner.get_product(Config.OPENFOODFACTS_DATA, "Boissons"):
        assert product == results
