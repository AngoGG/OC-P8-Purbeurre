from typing import List, Dict


class Config:

    OPENFOODFACTS_DATA = {
        "count": 9000,
        "page": "1",
        "page_size": "20",
        "products": [
            {
                "categories": "Boissons, Boissons gazeuses, Eaux, Eaux de sources, Eaux minérales, Boissons sans alcool, Eaux gazeuses, Eaux minérales naturelles, Eaux minérales gazeuses, Boissons sans sucre ajouté",
                "code": "3068320115160",
                "image_nutrition_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
                "image_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
                "nutriscore_grade": "a",
                "product_name": "La Salvetat",
                "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
                "nutriments": {
                    "bicarbonate": "0.053",
                    "bicarbonate_100g": "0.053",
                    "bicarbonate_label": "Bicarbonate",
                    "bicarbonate_unit": "mg",
                    "bicarbonate_value": 53,
                    "calcium": "0.016",
                    "calcium_100g": "0.016",
                    "calcium_label": "Calcium",
                    "calcium_unit": "mg",
                    "calcium_value": 16,
                    "carbohydrates": 0,
                    "carbohydrates_100g": 0,
                    "carbohydrates_unit": "g",
                    "carbohydrates_value": 0,
                    "chloride": "0.0005",
                    "chloride_100g": "0.0005",
                    "chloride_label": "Chloride",
                    "chloride_unit": "mg",
                    "chloride_value": "0.5",
                    "energy": 0,
                    "energy-kcal": 0,
                    "energy-kcal_100g": 0,
                    "energy-kcal_unit": "kcal",
                    "energy-kcal_value": 0,
                    "energy_100g": 0,
                    "energy_unit": "kcal",
                    "energy_value": 0,
                    "fat": 0,
                    "fat_100g": 0,
                    "fat_unit": "g",
                    "fat_value": 0,
                    "fiber": 0,
                    "fiber_100g": 0,
                    "fiber_unit": "g",
                    "fiber_value": 0,
                    "magnesium": "0.00075",
                    "magnesium_100g": "0.00075",
                    "magnesium_label": "Magnesium",
                    "magnesium_unit": "mg",
                    "magnesium_value": "0.75",
                    "nutrition-score-fr": 0,
                    "nutrition-score-fr_100g": 0,
                    "nutrition-score-uk": 0,
                    "nutrition-score-uk_100g": 0,
                    "potassium": "0.0002",
                    "potassium_100g": "0.0002",
                    "potassium_label": "Potassium",
                    "potassium_unit": "mg",
                    "potassium_value": "0.2",
                    "proteins": 0,
                    "proteins_100g": 0,
                    "proteins_unit": "g",
                    "proteins_value": 0,
                    "salt": "0.00127",
                    "salt_100g": "0.00127",
                    "salt_unit": "mg",
                    "salt_value": "1.27",
                    "saturated-fat": 0,
                    "saturated-fat_100g": 0,
                    "saturated-fat_unit": "g",
                    "saturated-fat_value": 0,
                    "silica": "0.0055",
                    "silica_100g": "0.0055",
                    "silica_label": "Silica",
                    "silica_unit": "mg",
                    "silica_value": "5.5",
                    "sodium": "0.000508",
                    "sodium_100g": "0.000508",
                    "sodium_unit": "mg",
                    "sodium_value": "0.508",
                    "sugars": 0,
                    "sugars_100g": 0,
                    "sugars_unit": "g",
                    "sugars_value": 0,
                    "sulfate": "0.002",
                    "sulfate_100g": "0.002",
                    "sulfate_label": "Sulfate",
                    "sulfate_unit": "mg",
                    "sulfate_value": 2,
                },
            }
        ],
        "skip": 0,
    }

    VALID_PRODUCT_DATA = {
        "categories": "Boissons, Boissons gazeuses, Eaux, Eaux de sources, Eaux minérales, Boissons sans alcool, Eaux gazeuses, Eaux minérales naturelles, Eaux minérales gazeuses, Boissons sans sucre ajouté",
        "code": "3068320115160",
        "image_nutrition_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
        "image_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutriscore_grade": "a",
        "product_name": "La Salvetat",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
    }

    PRODUCT_DATA_EMPTY_FIELD = {
        "categories": "Boissons, Boissons gazeuses, Eaux, Eaux de sources, Eaux minérales, Boissons sans alcool, Eaux gazeuses, Eaux minérales naturelles, Eaux minérales gazeuses, Boissons sans sucre ajouté",
        "code": "",
        "image_nutrition_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
        "image_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutriscore_grade": "a",
        "product_name": "La Salvetat",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
    }

    PRODUCT_DATA_MISSING_FIELD = {
        "categories": "Boissons, Boissons gazeuses, Eaux, Eaux de sources, Eaux minérales, Boissons sans alcool, Eaux gazeuses, Eaux minérales naturelles, Eaux minérales gazeuses, Boissons sans sucre ajouté",
        "image_nutrition_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
        "image_url": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutriscore_grade": "a",
        "product_name": "La Salvetat",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
    }

    PRODUCT_RESULTS = {
        "code": "3068320115160",
        "name": "La Salvetat",
        "nutriscore_grade": "a",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
        "image": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutrient_levels": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
        "carbohydrates_100g": 0,
        "fat_100g": 0,
        "proteins_100g": 0,
        "salt_100g": "0.00127",
        "saturated_fat_100g": 0,
        "sugars_100g": 0,
    }

    VALID_NUTRIMENTS_DATA = {
        "carbohydrates_100g": 0,
        "fat_100g": 0,
        "proteins_100g": 0,
        "salt_100g": "0.00127",
        "saturated_fat_100g": 0,
        "sugars_100g": 0,
    }

    NUTRIMENTS_DATA_MISSING_FIELD = {
        "fat_100g": 0,
        "proteins_100g": 0,
        "salt_100g": "0.00127",
        "saturated_fat_100g": 0,
        "sugars_100g": 0,
    }

    DATABASE_EXPECTED = {
        "code": "3068320115160",
        "name": "La Salvetat",
        "nutriscore_grade": "a",
        "url": "https://world.openfoodfacts.org/product/3068320115160/la-salvetat",
        "image": "https://static.openfoodfacts.org/images/products/306/832/011/5160/front_fr.131.400.jpg",
        "nutrient_levels": "https://static.openfoodfacts.org/images/products/306/832/011/5160/nutrition_fr.147.400.jpg",
        "carbohydrates_100g": 0,
        "fat_100g": 0,
        "proteins_100g": 0,
        "salt_100g": 0.00127,
        "saturated_fat_100g": 0,
        "sugars_100g": 0,
    }
