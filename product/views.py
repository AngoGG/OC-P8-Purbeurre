from django.shortcuts import render
from .models import Product, Category
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        products: Product = Product.objects.filter(name__contains=request.GET.get("search"))
        # category = Category.objects.get(name=request.GET.get("category"))
        # products = category.products.all()
        return render(request, "product/index.html", {"products": products})

def detail(request, code_product):
    product = Product.objects.get(code=code_product)
    return render(request, "product/detail.html", {"product": product})


