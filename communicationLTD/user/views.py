from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def login(request) -> HttpResponse:
    """ :return: Login html """
    return render(request, "user/login.html")


def register(request) -> HttpResponse:
    """ :return: Register html """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(requetst.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "user/register.html")


def forgot_password(request) -> HttpResponse:
    """ :return: Forgot Password html """
    return render(request, "user/forgot_password.html")
