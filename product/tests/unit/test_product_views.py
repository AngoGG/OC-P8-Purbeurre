import pytest
from django.test import Client, TestCase
from product.models import Product, Category
from product.views import IndexView
from tests.conftest import Config
from user.models import User


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


class TestSubstituteView(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_detail_get(self) -> None:
        client: Client = Client()
        product_code = "3068320115161"
        category = Category.objects.create(name="Boissons")
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)
            category.products.add(product["code"])
        response = client.get(f"/products/substitutes/{product_code}/")
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_detail_post(self) -> None:
        User.objects.create_user(
            email="test@mail.com",
            password="password8chars",
            first_name="firstname",
            last_name="lastname",
        )
        client: Client = Client()
        client.login(username="test@mail.com", password="password8chars")
        product_code = "3068320115161"
        category = Category.objects.create(name="Boissons")
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)
            category.products.add(product["code"])
        response = client.post(
            f"/products/substitutes/{product_code}/",
            {"product": "3068320115161", "substitute": "3068320115161",},
        )
        assert response.status_code == 200

