from django.db import models
from users.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя автора")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия автора")


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")


class Series(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название серии")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
