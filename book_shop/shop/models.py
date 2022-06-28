from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from books.models import Book


User = get_user_model()


class Cart(models.Model):
    """Модель для организации корзины"""
    user = models.ForeignKey(User, related_name="buyer",
                             verbose_name="Покупатель",
                             on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="books",
                             verbose_name="Книги",
                             on_delete=models.CASCADE)


class Rating(models.Model):
    """Модель для учета рейтинга книг"""
    user = models.ForeignKey(User, related_name="buyer",
                             verbose_name="Покупатель",
                             on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="books",
                             verbose_name="Книги",
                             on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(5)],
                                             verbose_name="Оценка")


class Favorite(models.Model):
    """Модель для организации списка желаемого"""
    user = models.ForeignKey(User, related_name="buyer",
                             verbose_name="Покупатель",
                             on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="books",
                             verbose_name="Книги",
                             on_delete=models.CASCADE)
