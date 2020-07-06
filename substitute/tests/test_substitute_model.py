import pytest
from django.test import TestCase
from product.models import Product
from substitute.models import Substitute
from tests.conftest import Config
from user.models import User


class TestSubstitute(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_add_favorite(self) -> None:
        user = User.objects.create_user(
            email="test@mail.com",
            password="password8chars",
            first_name="firstname",
            last_name="lastname",
        )
        product_code = "3068320115160"
        code_substitute = "3068320115161"
        for product in Config.PRODUCT_AND_SUBSTITUTE_DATA["product"]:
            Product.objects.create(**product)

        product = Product.objects.filter(code=product_code).first()
        substitute = Product.objects.filter(code=code_substitute).first()

        Substitute.add_favorite(user, product, substitute)
        substitutes = Substitute.objects.filter(user=user)
        assert len(substitutes) == 1
        for substitute in substitutes:
            assert substitute.user.email == "test@mail.com"
            assert substitute.product.code == product_code
            assert substitute.substitute.code == code_substitute
