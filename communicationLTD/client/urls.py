from django.urls import path

from . import views

urlpatterns = [
    path("", views.clients, name="clients"),
    path("create_client/", views.create_client, name="create_client"),
]