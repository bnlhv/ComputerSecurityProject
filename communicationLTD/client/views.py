from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Client
from .utils import create_client_with_sqli_demonstration


@login_required(login_url="login")
def clients(request) -> HttpResponse:
    """ :return: All clients """
    all_clients = Client.objects.all()
    return render(request, "client/clients.html", {"clients": all_clients})


@login_required(login_url="login")
def create_client(request) -> HttpResponse:
    """ Post method for creating new client """
    form = ClientForm()
    if request.method == "POST":

        # With sql injection demontration

        # full_name = request.POST.get("full_name")
        # email = request.POST.get("email")
        # data_package = request.POST.get("data_package")
        # sectors = request.POST.get("sectors")
        #
        # create_client_with_sqli_demonstration(
        #     full_name=full_name,
        #     email=email,
        #     data_package=data_package,
        #     sectors=sectors
        # )

        # Without sql injection

        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients/")

    context = {"form": form}
    return render(request, "client/create_client_form.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
def delete_client(request, pk) -> HttpResponse:
    """ Delete method for deleting existing client """
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect("/clients/")
    context = {"client": client}
    return render(request, "client/delete_client_form.html", context)
