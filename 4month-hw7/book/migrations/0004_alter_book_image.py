# Generated by Django 4.1.7 on 2023-02-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_description_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото книги:'),
        ),
    ]