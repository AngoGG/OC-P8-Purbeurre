from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
    return render(request, "search.html")


def detail(request, code_product):
    product = Product.objects.get(code=code_product)
    return render(request, "detail.html", {"product": product})


def index(request):
    category = Category.objects.get(name=request.GET.get("category"))
    products = category.products.all()
    return render(request, "index.html", {"products": products})
