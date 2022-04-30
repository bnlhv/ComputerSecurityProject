from django.urls import path

from . import views

urlpatterns = [
    path("", views.clients, name="clients"),
    path("create_client/", views.create_client, name="create_client"),
    path("update_client/<str:pk>/", views.update_client, name="update_client"),
    path("delete_client/<str:pk>/", views.delete_client, name="delete_client"),
]