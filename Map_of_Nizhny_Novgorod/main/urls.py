from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('map_view', views.map_view, name='map_view'),
]
