# Generated by Django 2.2.13 on 2020-06-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200628_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kcal_100g',
            field=models.FloatField(null=True),
        ),
    ]
