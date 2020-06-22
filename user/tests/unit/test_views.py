import pytest
from django.test import Client, TestCase
from user.models import User
from user.views import RegistrationView


class TestRegistrationView(TestCase):
    def test_register_post(self) -> None:
        client: Client = Client()
        response = client.post(
            "/user/register",
            {
                "email": "user-name@gmail.com",
                "first_name": "user",
                "last_name": "name",
                "password1": "password8chars",
                "password2": "password8chars",
                "submit": "Register",
            },
        )
        assert response.status_code == 302  # Testing redirection
        user_created: User = User.objects.first()  # type: ignore
        self.assertEqual("user-name@gmail.com", user_created.email)
        self.assertTrue(user_created.check_password("password8chars"))
        self.assertEqual("user", user_created.first_name)
        self.assertEqual("name", user_created.last_name)

    def test_register_get(self) -> None:
        client: Client = Client()
        response = client.get("/user/register")
        assert response.status_code == 200  # Testing redirection

