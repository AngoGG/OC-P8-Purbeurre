from django.core.management.base import BaseCommand

from product.models import Category, Product
from openfoodfacts.api import Api, DataCleaner


class Command(BaseCommand):
    help = "Lance la récupération des données de l'API OpenFoodFacts pour remplir la base de données PurBeurre"

    def handle(self, *args, **options):
        print("Lancement de la récupération des données de l'API OFF")

        CATEGORIES = [
            "Sodas",
        ]
        api: Api = Api()
        clean_datas: DataCleaner = DataCleaner()
        Product.objects.all().delete()
        Category.objects.all().delete()
        for category in CATEGORIES:
            result = api.get_data(category)
            category = Category.objects.create(name=category)
            for product in clean_datas.get_product(result, category):
                print(product["code"])
                Product.objects.create(**product)
                category.products.add(product["code"])
