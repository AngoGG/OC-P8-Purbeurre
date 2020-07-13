from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from .models import Substitute
from user.models import User


class FavoritesSubstituteViews(LoginRequiredMixin, ListView):
    def get(self, request):
        user: User = request.user
        favorites = Substitute.get_favorite(user)
        return render(
            request, "substitute/favorites_substitutes.html", {"products": favorites,},
        )
