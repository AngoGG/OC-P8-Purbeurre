import requests
from typing import Dict
from openfoodfacts.api import Api
from tests.conftest import Config


class MockResponse:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json() -> Dict:
        return Config.OPENFOODFACTS_DATA


def test_get_data(monkeypatch) -> None:
    """ Method testing data recovery via the OpenFoodFacts API """
    api: Api = Api()

    def mockreturn(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mockreturn)
    assert api.get_data("Boissons") == Config.OPENFOODFACTS_DATA
