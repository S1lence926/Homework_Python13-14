from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_read")
    list_filter = ("is_read",)
    search_fields = ("title", "author")
    list_editable = ("is_read",)
    ordering = ("-id",)
