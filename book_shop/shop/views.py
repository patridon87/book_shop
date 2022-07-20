from django.shortcuts import render
from books.models import Book


def index(request):
    # books = [{"image": "Здесь будет картинка",
    #           "name": "Как написать бэкенд на питоне",
    #           "author": "Андрей Пронин",
    #           "price": 1200}] * 3
    books = Book.objects.order_by('catalog_add_date')[:6]
    context = {"books": books}
    return render(request, "index.html", context)
