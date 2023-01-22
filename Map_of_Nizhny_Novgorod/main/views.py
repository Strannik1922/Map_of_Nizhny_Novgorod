from django.shortcuts import render
from .map_creator import map_create


def index(request):
    map_create('./templates/main/map_view.html')
    return render(request, 'main/index.html')


def map_view(request):
    return render(request, 'main/map_view.html')
