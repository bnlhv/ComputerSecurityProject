from django.http import HttpResponse
from django.shortcuts import render

from .models import Client


def clients(request) -> HttpResponse:
    """ :return: All clients """
    all_clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": all_clients})
