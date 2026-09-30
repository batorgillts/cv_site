"""Project-level URL configuration.

Every request starts here. Anything that isn't /admin/ is handed
to the cv app's own urls.py via include().
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cv.urls")),
]
