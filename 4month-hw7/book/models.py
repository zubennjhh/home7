from django.db import models


class Book(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('ROMAN', 'ROMAN'),
        ('DETECTIVE', 'DETECTIVE'),
        ('ADVENTURE', 'ADVENTURE'),
        ('DRAMATIC', 'DRAMATIC'),
    )

    title = models.CharField('Название книги:', max_length=200, null=True)
    description = models.TextField('Описание книги:', null=True)
    quantity = models.PositiveIntegerField('Количество страниц:', null=True)
    image = models.ImageField('Фото книги:', upload_to='', null=True)
    genre = models.CharField('Жанр:', max_length=100, choices=GENRE, null=True)
    link = models.URLField('Ссылка на книгу:', null=True)
    price = models.PositiveIntegerField('Цена:', null=True)
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class RatingBook(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_object')
    rate = models.IntegerField('Оценка: ', choices=RATING)
    comment = models.TextField('Комментарий: ')
    created_date = models.DateTimeField(auto_now_add=True)