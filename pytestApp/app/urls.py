from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.fetch_clients, name="list of clients"),
    path('clients/<int:id>', views.client_details),
    path('clients/<int:id>/projects', views.create_project),
    path('projects', views.fetch_projects),
   
]   