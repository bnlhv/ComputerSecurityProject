from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('register/', views.register),
    path('forgot_password/', views.forgot_password),
]