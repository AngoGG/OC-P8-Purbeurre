from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def index(request):
    category = Category.objects.get(name="Sodas")
    products = category.products.all()
    return render(request, "index.html", {"products": products})


def detail(request, code_product):
    product = Product.objects.get(code=code_product)
    return render(request, "detail.html", {"product": product})
