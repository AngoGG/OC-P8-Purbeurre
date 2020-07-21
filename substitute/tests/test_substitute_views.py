import json
import pytest
from django.http import HttpResponse
from django.test import Client, TestCase
from product.views import Product, Category
from substitute.views import FavoritesSubstituteView, FavoriteSaveView
from tests.conftest import Config
from user.models import User


class TestFavoritesSubstituteView(TestCase):
    def test_favorites_substitutes(self) -> None:
        User.objects.create_user(
            email="test@mail.com",
            password="password8chars",
            first_name="firstname",
            last_name="lastname",
        )
        client: Client = Client()
        client.login(username="test@mail.com", password="password8chars")
        response = client.get("/favorites/",)
        assert response.status_code == 200  # Testing redirection

    def test_favorites_substitutes_not_connected(self) -> None:
        client: Client = Client()
        response = client.get("/favorites/",)
        assert response.status_code == 302  # Testing redirection


class TestFavoriteSaveView(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_add_favorite(self) -> None:
        User.objects.create_user(
            email="test@mail.com",
            password="password8chars",
            first_name="firstname",
            last_name="lastname",
        )
        client: Client = Client()
        client.login(username="test@mail.com", password="password8chars")
        category = Category.objects.create(name="Boissons")
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)
            category.products.add(product["code"])

        response: HttpResponse = client.post(
            "/favorites/add",
            {"product": "3068320115161", "substitute": "3068320115161",},
        )
        json_response: str = json.loads(response.content.decode("utf-8"))[
            "favori_added"
        ]

        self.assertEqual(json_response, "success")

    def test_add_favorite_not_connected(self) -> None:
        User.objects.create_user(
            email="test@mail.com",
            password="password8chars",
            first_name="firstname",
            last_name="lastname",
        )
        client: Client = Client()
        category = Category.objects.create(name="Boissons")
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)
            category.products.add(product["code"])

        response: HttpResponse = client.post(
            "/favorites/add",
            {"product": "3068320115161", "substitute": "3068320115161",},
        )
        self.assertEqual(response.status_code, 302)
