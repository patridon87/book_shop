from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя автора")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия автора")
    bio = models.TextField(verbose_name="Краткая биография автора")


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")


class Series(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название серии")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название книги")
    author = models.ForeignKey(Author, verbose_name="Автор книги",
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to="books/",
                              verbose_name="Изображение книги")
    series = models.ForeignKey(Series, on_delete=models.SET_NULL,
                               verbose_name="Серия")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                               verbose_name="Категория")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,
                               verbose_name="Жанр")
    publishing_year = models.PositiveSmallIntegerField(
        verbose_name="Год публикации книги")
    publishing_house = models.CharField(max_length=150,
                                        verbose_name="Издательство")
    format = models.CharField(max_length=150, verbose_name="Формат")
    cover = models.CharField(max_length=150, verbose_name="Тип обложки")
    catalog_add_date = models.DateField(auto_now_add=True)
