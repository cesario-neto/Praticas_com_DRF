from django.db import models
from bookshelves.models import BookShelf


class Author(models.Model):
    name = models.CharField(max_length=115)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class ImportAuthor(models.Model):
    file = models.FileField(upload_to='imports/author/%Y/%m')
    finish = models.BooleanField(default=False)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=True, null=True)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='book/%Y/%m', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.ForeignKey(
        BookShelf, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class ImportBook(models.Model):
    file = models.FileField(upload_to='imports/book/%Y/%m')
    finish = models.BooleanField(default=False)
