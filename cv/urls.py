"""URL routes for the cv app.

app_name + name give each route a nickname like "cv:home",
which templates use with {% url %} instead of hardcoded paths.
"""
from django.urls import path

from . import views

app_name = "cv"

urlpatterns = [
    path("", views.cv_page, name="home"),
    path("contact/", views.contact_page, name="contact"),
]
