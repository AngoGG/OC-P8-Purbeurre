import pytest
from django.test import TestCase
from user.models import User


class TestUserManager(TestCase):
    def test__create_user(self) -> None:
        user: User = User.objects._create_user(
            email="mail@mail.com", password="password", first_name="firstname", last_name="lastname"
        )
        user_created: User = User.objects.first()  # type: ignore
        self.assertEqual(user, user_created)
        self.assertEqual("mail@mail.com", user_created.email)
        self.assertTrue(user_created.check_password("password"))
        self.assertEqual("firstname", user_created.first_name)
        self.assertEqual("lastname", user_created.last_name)

    def test_create_user(self) -> None:
        user: User = User.objects.create_user(
            email="mail@mail.com", password="password", first_name="firstname", last_name="lastname")
        user_created: User = User.objects.first()
        self.assertEqual(user, user_created)
        self.assertEqual("mail@mail.com", user_created.email)
        self.assertTrue(user_created.check_password("password"))
        self.assertEqual("firstname", user_created.first_name)
        self.assertEqual("lastname", user_created.last_name)
        self.assertFalse(user_created.is_superuser)
 

    def test_create_superuser(self) -> None:
        user: User = User.objects.create_superuser(
            email="mail@mail.com", password="password", first_name="firstname", last_name="lastname")
        user_created: User = User.objects.first()
        self.assertEqual(user, user_created)
        self.assertEqual("mail@mail.com", user_created.email)
        self.assertTrue(user_created.check_password("password"))
        self.assertEqual("firstname", user_created.first_name)
        self.assertEqual("lastname", user_created.last_name)
        self.assertTrue(user_created.is_superuser)
