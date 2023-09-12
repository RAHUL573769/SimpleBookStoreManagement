from django.shortcuts import render
from bookapp.forms import BookForm
from django.shortcuts import redirect
from bookapp.models import BookStoreModel


# Create your views here.
def homepage(request):
    return render(request, "base.html")


def store_books(request):
    print("Hello")
    if request.method == "POST":
        print("Hello1")
        book = BookForm(request.POST)
        if book.is_valid():
            print("Hello 3")
            book.save(commit=True)
            print(book.cleaned_data)
            return redirect("show_book")
    else:
        book = BookForm()
        print(book)
    return render(request, "store_book.html", {"form": book})


def show_books(request):
    book = BookStoreModel.objects.all()
    print(book)
    for item in book:
        print(item.first_pub)
    return render(request, "show_book.html", {"data": book})


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        info = BookForm(request.POST, instance=book)
        if info.is_valid():
            book.save()
            return redirect("show_book")
    return render(request, "store_book.html", {"form": form})
