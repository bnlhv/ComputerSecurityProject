from django.urls import path

from . import views

urlpatterns = [
    path("", views.loginPage),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("forgot_password/", views.forgotPasswordPage, name="forgot_password"),
]
