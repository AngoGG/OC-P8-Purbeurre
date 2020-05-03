import requests
from openfoodfacts.api import Api
from tests.conftest import Config


def test_get_data(monkeypatch) -> None:
    """ Method testing data recovery via the OpenFoodFacts API """
    results = Config.OPENFOODFACTS_DATA
    api: Api = Api()

    def mockreturn(self):
        return results

    monkeypatch.setattr(Api, "request", mockreturn)
    assert api.get_data("Boissons") == results
