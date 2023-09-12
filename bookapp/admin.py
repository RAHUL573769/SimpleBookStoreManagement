from django.contrib import admin
from bookapp.models import BookStoreModel


class BookStoreAdmin(admin.ModelAdmin):
    list_display = ("id", "book_name", "author", "category")


admin.site.register(BookStoreModel, BookStoreAdmin)
