from django.db import models

# Create your models here.


class Product(models.Model):
    code: models.CharField = models.CharField(
        primary_key=True, max_length=55, blank=False, unique=True
    )
    name: models.CharField = models.CharField(max_length=255, blank=False)
    nutriscore_grade: models.CharField = models.CharField(max_length=1, blank=False)
    url: models.CharField = models.CharField(max_length=255, blank=False)
    image: models.URLField = models.URLField(max_length=255, blank=False)
    nutrient_levels: models.URLField = models.URLField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=255, blank=False, unique=True)
    products: models.ManyToManyField = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
