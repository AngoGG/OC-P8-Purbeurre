from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from . import views

app_name: str = "substitute"

urlpatterns = [
    url(r"^$", views.FavoritesSubstituteViews.as_view(), name="favorites",),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
