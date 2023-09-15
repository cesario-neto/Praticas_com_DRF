import os
import csv

from bookshelves.models import BookShelf


def gender_import(obj: BookShelf | None, model: BookShelf):
    if obj:
        file_url = obj.file.path
        file, extension = os.path.splitext(obj.file.url)

        if extension == '.csv':
            with open(file_url, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for i in reader:
                    if model.objects.filter(name=i.get('name')).exists():
                        print('Já existe')
                    else:
                        book = model(name=i.get('name'))
                        book.save()

        obj.finish = True
        obj.save()
