# Generated by Django 4.2.5 on 2023-09-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0002_importbookshelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='importbookshelf',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
