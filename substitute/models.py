from django.db import models
from product.models import Product
from user.models import User

# Create your models here.


class Substitute(models.Model):
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    product: models.ForeignKey = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product",
    )
    substitute: models.ForeignKey = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="substitute",
    )

