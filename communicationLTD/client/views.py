from django.http import HttpResponse
from django.shortcuts import render

def clients(request) -> HttpResponse:
    """ :return: All clients """
    return render(request, "client/clients.html")
