from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("storebook/", views.store_books, name="store_book"),
    path("showbook/", views.show_books, name="show_book"),
    path("edit_book/<int:id>", views.edit_book, name="edit_book"),
]
