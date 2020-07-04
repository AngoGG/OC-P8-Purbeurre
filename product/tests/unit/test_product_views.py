import pytest
from django.test import Client, TestCase
from product.models import Product, Category
from product.views import IndexView
from tests.conftest import Config


class TestIndexView(TestCase):
    def test_index_get(self) -> None:
        client: Client = Client()
        response = client.get("/products/search/", {"search": "Product Name",},)
        assert response.status_code == 200


class TestDetailView(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_detail_get(self) -> None:
        client: Client = Client()
        Product.objects.create(**Config.DATABASE_EXPECTED)
        code_product = Config.DATABASE_EXPECTED["code"]
        response = client.get(f"/products/{code_product}/")
        assert response.status_code == 200
