from django.contrib import admin
from .models import BookShelf, ImportBookShelf
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.gender_imports import gender_import


@admin.register(BookShelf)
class BookShelfAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'id', 'name',
    search_fields = 'name',


@admin.register(ImportBookShelf)
class ImportBookShelfAdmin(admin.ModelAdmin):
    list_display = 'id', 'file', 'finish',
    list_display_links = 'id', 'file',


@receiver(post_save, sender=ImportBookShelf)
def import_gender(sender: BookShelf, **kwargs):
    obj = sender.objects.filter(finish=False).first()
    gender_import(obj, BookShelf)
