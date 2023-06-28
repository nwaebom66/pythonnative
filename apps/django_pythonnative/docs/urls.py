from django.urls import path

from . import views

app_name = "docs"
urlpatterns = [
    path("", views.index, name="index"),
    path("install", views.install, name="install"),
    path("introduction", views.introduction, name="introduction"),
    path("native-apis", views.native_apis, name="native-apis"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("views", views.views, name="views"),
]
