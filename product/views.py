from django.shortcuts import render
from .models import Product, Category
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        products: Product = Product.objects.filter(
            nutriscore_grade__gt="c", name__contains=request.GET.get("search")
        )
        return render(request, "product/index.html", {"products": products})


class DetailView(View):
    def get(self, request, code_product):
        product = Product.objects.get(code=code_product)
        return render(request, "product/detail.html", {"product": product})

