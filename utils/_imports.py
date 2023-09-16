import os
import csv

from bookshelves.models import BookShelf
from books.models import Author, Book


def gender_import(obj: BookShelf | None, model: BookShelf):
    if obj:
        file_path = obj.file.path
        file, extension = os.path.splitext(obj.file.url)

        if extension == '.csv':
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for i in reader:
                    if model.objects.filter(name=i.get('name')).exists():
                        ...
                    else:
                        book = model(name=i.get('name'))
                        book.save()

        obj.finish = True
        obj.save()


def authors_import(instance: Author, model: Author):
    if instance.finish is False:
        file, extension = os.path.splitext(instance.file.url)
        if extension == '.csv':
            file_path = instance.file.path
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for i in reader:
                    name = i.get('name')
                    age = i.get('age')
                    name_exists = model.objects.filter(name=name).exists()
                    age_exists = model.objects.filter(age=age).exists()
                    if name_exists and age_exists:
                        ...
                    else:
                        author = model(name=name, age=age)
                        author.save()
        instance.finish = True
        instance.save()


def books_import(instance: Book, model: Book):
    if instance.finish is False:
        file, extension = os.path.splitext(instance.file.url)

        if extension == '.csv':
            file_path = instance.file.path
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for i in reader:
                    title = i.get('title')
                    pages = i.get('pages')
                    price = i.get('price')
                    gender = get_gender(BookShelf, i.get('gender'))
                    author = get_author(Author, i.get('author'))
                    if model.objects.filter(title=title, author=author).exists():
                        ...
                    else:
                        book = model(title=title, author=author,
                                     pages=pages, price=price, gender=gender)
                        book.save()
        instance.finish = True
        instance.save()


def get_gender(model, gender_name):
    gender = model.objects.get(name=gender_name)
    if gender:
        return gender
    else:
        return None


def get_author(model, author_name):
    author = model.objects.get(name=author_name)
    if author:
        return author
    else:
        return None
