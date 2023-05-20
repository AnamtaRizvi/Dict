from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("edit", views.edit, name="edit"),
    path("create", views.create, name="create"),
    path("new", views.new, name="new"),
    path("search", views.search, name="search"),
    path("<str:title>", views.title, name="title")
    
]   
