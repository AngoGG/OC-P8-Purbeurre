from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from . import views

urlpatterns = [
    # path(r"", views.index, name="index"),
    path(r"", views.home, name="home"),
    path(r"search/", views.index, name="index"),
    path(r"<int:code_product>/", views.detail, name="detail"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
