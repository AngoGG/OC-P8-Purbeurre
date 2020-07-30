from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product, Category
from .views import Product
from substitute.models import Substitute

# Create your views here.
class IndexView(View):
    def get(self, request):
        products: Product = Product.objects.filter(
            name__istartswith=request.GET.get("search")
        ).order_by("-nutriscore_grade")
        return render(request, "product/index.html", {"products": products})


class DetailView(View):
    def get(self, request, code_product):
        product = Product.objects.get(code=code_product)
        return render(request, "product/detail.html", {"product": product})


class SubstituteIndexView(View):
    def get(self, request, code_product):
        product = Product.objects.get(code=code_product)
        substitutes = Product.get_substitute(code_product)
        user_favorite_list = []
        if request.user.is_authenticated:
            user_favorites = Substitute.get_favorite(request.user)
            for favorite in user_favorites:
                user_favorite_list.append(favorite.substitute_id)
        return render(
            request,
            "product/substitutes_index.html",
            {
                "product_code": code_product,
                "product_name": product.name,
                "substitutes": substitutes,
                "favorites": user_favorite_list,
            },
        )
