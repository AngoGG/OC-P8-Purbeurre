import pytest
from django.test import Client, TestCase
from app.views import HomeView

class TestHomeView(TestCase):
    def test_home_get(self) -> None:
        client: Client = Client()
        response = client.get("/",)
        assert response.status_code == 200  # Testing redirection