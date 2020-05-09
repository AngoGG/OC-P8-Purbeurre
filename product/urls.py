from django.conf.urls import include, url
from django.conf import settings
from . import views

urlpatterns = [
    url(r"^", views.index),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
