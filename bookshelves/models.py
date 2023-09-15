from django.db import models


class BookShelf(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class ImportBookShelf(models.Model):
    file = models.FileField(upload_to='imports/bookshelf/%Y/%m')
    finish = models.BooleanField(default=False)
