from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookModelTest(TestCase):
    def test_str_returns_title(self):
        book = Book(title="Дюна", author="Фрэнк Герберт", description="Фантастика")
        self.assertEqual(str(book), "Дюна")

    def test_is_read_is_false_by_default(self):
        book = Book.objects.create(
            title="Дюна",
            author="Фрэнк Герберт",
            description="Фантастика",
        )
        self.assertFalse(book.is_read)


class BookViewsTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="1984",
            author="Джордж Оруэлл",
            description="Антиутопия",
            is_read=True,
        )
        Book.objects.create(
            title="Дюна",
            author="Фрэнк Герберт",
            description="Фантастика",
            is_read=False,
        )

    def test_book_list_shows_books_and_statuses(self):
        response = self.client.get(reverse("books:book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1984")
        self.assertContains(response, "Дюна")
        self.assertContains(response, "Прочитана")
        self.assertContains(response, "Ещё не прочитана")
        self.assertContains(response, "Всего: 2")

    def test_book_create_get_shows_empty_form(self):
        response = self.client.get(reverse("books:book_create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Добавить книгу")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_book_create_post_saves_book_and_redirects(self):
        response = self.client.post(
            reverse("books:book_create"),
            {
                "title": "Тень ветра",
                "author": "Карлос Руис Сафон",
                "description": "История о забытой книге",
            },
        )

        self.assertRedirects(response, reverse("books:book_list"))
        self.assertTrue(Book.objects.filter(title="Тень ветра").exists())

    def test_book_create_post_with_errors_does_not_save(self):
        response = self.client.post(
            reverse("books:book_create"),
            {"title": "", "author": "", "description": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 2)

    def test_empty_state_message(self):
        Book.objects.all().delete()

        response = self.client.get(reverse("books:book_list"))

        self.assertContains(response, "Вы пока не добавили ни одной книги")
