from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Client


def clients(request) -> HttpResponse:
    """ :return: All clients """
    all_clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": all_clients})


def create_client(request) -> HttpResponse:
    """ Post method for creating new client """
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
    context = {"form": form}
    return render(request, "client/create_client_form.html", context)


def update_client(request, pk) -> HttpResponse:
    """ Update method for updating existing client """
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
    context = {"form": form}
    return render(request, "client/create_client_form.html", context)


def delete_client(request, pk) -> HttpResponse:
    """ Delete method for deleting existing client """
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect("/clients/")
    context = {"client": client}
    return render(request, "client/delete_client_form.html", context)
