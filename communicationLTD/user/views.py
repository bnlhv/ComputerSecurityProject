from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CreateUserForm


def login_page(request) -> HttpResponse:
    """:return: Login html"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("clients")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "user/login.html")


def register_page(request) -> HttpResponse:
    """:return: Register html"""
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered succesfully")
            return redirect("login")

    context = {"form": form}
    return render(request, "user/register.html", context)


def forgot_password_page(request) -> HttpResponse:
    """:return: Forgot Password html"""
    return render(request, "user/forgot_password.html")
