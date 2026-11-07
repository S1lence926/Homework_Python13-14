from django.db import models


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=150)
    description = models.TextField("Краткое описание")
    is_read = models.BooleanField("Прочитана", default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
