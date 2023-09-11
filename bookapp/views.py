from django.shortcuts import render
from bookapp.forms import BookForm


# Create your views here.
def homepage(request):
    return render(request, "base.html")


def store_books(request):
    book = BookForm
    return render(request, "store_book.html", {"form": book})
