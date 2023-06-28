from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "docs/index.html")


def install(request: HttpRequest) -> HttpResponse:
    return render(request, "docs/install.html")


def introduction(request: HttpRequest) -> HttpResponse:
    return render(request, "docs/introduction.html")


def tutorial(request: HttpRequest) -> HttpResponse:
    return render(request, "docs/tutorial.html")