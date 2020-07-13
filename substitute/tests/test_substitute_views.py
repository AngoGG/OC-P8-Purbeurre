import pytest
from django.test import Client, TestCase
from substitute.views import FavoritesSubstituteViews
from user.models import User


class TestFavoritesSubstituteViews(TestCase):
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
