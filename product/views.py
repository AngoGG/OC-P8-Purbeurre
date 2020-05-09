from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def index(request):
    category = Category.objects.get(name="Sodas")
    products = category.products.all()
    print(products)
    return render(request, "index.html", {"products": products})
