from django.contrib import admin
from .models import Author, Book, ImportAuthor, ImportBook
from bookshelves.models import BookShelf
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils._imports import authors_import, books_import


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'name', 'age',
    search_fields = 'name',


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'title', 'author', 'price', 'gender',
    search_fields = 'title', 'author', 'gender',
    list_filter = 'gender',


@admin.register(ImportAuthor)
class ImportAuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'file', 'finish',
    list_display_links = 'id', 'file',


@admin.register(ImportBook)
class ImportBooksAdmin(admin.ModelAdmin):
    list_display = 'id', 'file', 'finish',
    list_display_links = 'id', 'file',


@receiver(post_save, sender=ImportAuthor)
def import_author(sender, **kwargs):
    instance = kwargs.get('instance')
    authors_import(instance, Author)


@receiver(post_save, sender=ImportBook)
def import_book(sender, **kwargs):
    instance = kwargs.get('instance')
    books_import(instance, Book)
