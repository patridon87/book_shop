from django.contrib import admin

from .models import Book, Author, Category, Genre, Series


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'in_stock', 'category', 'genre')
    search_fields = ('title', 'author')
    empty_value_display = '-пусто-'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Series, SeriesAdmin)
