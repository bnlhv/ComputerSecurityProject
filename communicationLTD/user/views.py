from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import CreateUserForm

class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("clients")
    template_name = "user/change_password.html"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def login_page(request) -> HttpResponse:
    """:return: Login html"""
    if request.user.is_authenticated:
        return redirect("clients")
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
    if request.user.is_authenticated:
        return redirect("clients")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
            return redirect("login")

    context = {"form": form}
    return render(request, "user/register.html", context)


@login_required(login_url='login')
def logout_page(request) -> HttpResponse:
    """:return: logout user"""
    logout(request)
    return redirect("login")
