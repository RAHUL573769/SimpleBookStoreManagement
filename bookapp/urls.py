from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("storebook/", views.store_books, name="store_book"),
]
