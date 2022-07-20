from django.db import models


class Author(models.Model):
    """Модель авторов книг"""
    name = models.CharField(max_length=1500,
                            verbose_name="ФИО Автора или авторов")
    bio = models.TextField(blank=True, null=True,
                           verbose_name="Краткая биография автора")

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категорий книг"""
    name = models.CharField(max_length=150, verbose_name="Название категории")

    def __str__(self):
        return self.name



class Genre(models.Model):
    """Модель жанров книг"""
    name = models.CharField(max_length=150, verbose_name="Название жанра")

    def __str__(self):
        return self.name



class Series(models.Model):
    """Модель серий книг"""
    name = models.CharField(max_length=150, verbose_name="Название серии")
    author = models.ForeignKey(Author, related_name='series',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Book(models.Model):
    """Модель книг"""
    title = models.CharField(max_length=300, verbose_name="Название книги")
    author = models.ForeignKey(Author, related_name='books',
                               verbose_name="Автор книги",
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to="books/",
                              verbose_name="Изображение книги")
    series = models.ForeignKey(Series, related_name='books',
                               on_delete=models.SET_NULL,
                               verbose_name="Серия", blank=True, null=True)
    category = models.ForeignKey(Category, related_name='books',
                                 on_delete=models.SET_NULL,
                                 verbose_name="Категория", null=True)
    genre = models.ForeignKey(Genre, related_name='books',
                              on_delete=models.SET_NULL,
                              verbose_name="Жанр", null=True)
    publishing_year = models.PositiveSmallIntegerField(
        verbose_name="Год публикации книги")
    publishing_house = models.CharField(max_length=150,
                                        verbose_name="Издательство")
    format = models.CharField(max_length=150, verbose_name="Формат")
    cover = models.CharField(max_length=150, verbose_name="Тип обложки")
    catalog_add_date = models.DateField(auto_now_add=True)
    in_stock = models.PositiveSmallIntegerField(
        verbose_name="Количество на складе")
    number_of_sold = models.PositiveIntegerField(
        verbose_name="Количество проданных экземпляров", default=0)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    def set_number_of_sold(self, solded):
        self.number_of_sold += solded
