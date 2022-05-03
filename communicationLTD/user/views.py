import imp
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CreateUserForm


def loginPage(request) -> HttpResponse:
    """:return: Login html"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("login")
        else:
            messages.error(request, "Invalid credentials")

    context = {}
    return render(request, "user/login.html")


def registerPage(request) -> HttpResponse:

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


def forgotPasswordPage(request) -> HttpResponse:
    """:return: Forgot Password html"""
    return render(request, "user/forgot_password.html")
