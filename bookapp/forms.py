from django import forms
from bookapp.models import BookStoreModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ["id", "book_name", "author", "category"]
