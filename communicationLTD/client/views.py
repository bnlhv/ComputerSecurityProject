from django.http import HttpResponse
from django.shortcuts import render

from .forms import ClientForm
from .models import Client


def clients(request) -> HttpResponse:
    """ :return: All clients """
    all_clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": all_clients})


def create_client(request) -> HttpResponse:
    """ Post method for creating new client """
    form = ClientForm()
    context = {"form": form}
    return render(request, "client/create_client_form.html", context)
