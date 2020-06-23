from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from . import views

app_name: str = "product"

urlpatterns = [
    path(r"search/", views.IndexView.as_view(), name="index"),
    path(r"<int:code_product>/", views.detail, name="detail"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
