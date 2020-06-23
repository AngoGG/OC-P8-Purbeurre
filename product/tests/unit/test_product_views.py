import pytest
from django.test import Client, TestCase
from product.models import Product, Category
from product.views import IndexView
from tests.conftest import Config


class TestIndexView(TestCase):
    def test_index_get(self) -> None:
        client: Client = Client()
        response = client.get(
            "/products/search/",
            {"search": "Product Nam",},
        )
        assert response.status_code == 200