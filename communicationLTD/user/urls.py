from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register_page, name="register"),
    path("forgot_password/", views.forgot_password_page, name="forgot_password"),
]
