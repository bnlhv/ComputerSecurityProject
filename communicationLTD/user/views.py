from django.http import HttpResponse
from django.shortcuts import render


def login(request) -> HttpResponse:
    """ :return: Login html """
    return render(request, "user/login.html")


def register(request) -> HttpResponse:
    """ :return: Register html """
    return render(request, "user/register.html")


def forgot_password(request) -> HttpResponse:
    """ :return: Forgot Password html """
    return render(request, "user/forgot_password.html")
