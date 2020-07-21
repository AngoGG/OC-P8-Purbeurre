from django.http import JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View
from product.models import Product, Category
from product.views import Product
from .models import Substitute
from user.models import User


class FavoritesSubstituteView(LoginRequiredMixin, ListView):
    def get(self, request):
        user: User = request.user
        favorites = Substitute.get_favorite(user)
        return render(
            request, "substitute/favorites_substitutes.html", {"products": favorites,},
        )


class FavoriteSaveView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        product = Product.objects.filter(code=request.POST.get("product")).first()
        substitute = Product.objects.filter(code=request.POST.get("substitute")).first()
        Substitute.add_favorite(user, product, substitute)
        return JsonResponse({"favori_added": "success",})
