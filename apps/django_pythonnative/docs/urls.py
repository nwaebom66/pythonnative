from django.urls import path

from . import views

app_name = "docs"
urlpatterns = [
    path("", views.index, name="index"),
    path("install", views.install, name="install"),
    path("introduction", views.introduction, name="introduction"),
]
