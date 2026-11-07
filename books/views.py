from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


def book_list(request):
    """Показывает все книги из базы данных."""
    books = Book.objects.all()

    context = {
        "books": books,
        "total_books": books.count(),
        "read_books": books.filter(is_read=True).count(),
        "unread_books": books.filter(is_read=False).count(),
    }
    return render(request, "books/book_list.html", context)


def book_create(request):
    """Показывает пустую форму и сохраняет новую книгу после POST-запроса."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f"Книга «{book.title}» добавлена на полку.")
            return redirect("books:book_list")
    else:
        form = BookForm()

    return render(request, "books/book_form.html", {"form": form})
