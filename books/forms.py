from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "is_read"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Например, «Мастер и Маргарита»",
                    "autofocus": True,
                }
            ),
            "author": forms.TextInput(
                attrs={"placeholder": "Например, Михаил Булгаков"}
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "О чём эта книга и почему вы её выбрали",
                }
            ),
        }
