from django.shortcuts import render


def index(request):
    books = [{"image": "Здесь будет картинка",
              "name": "Как написать бэкенд на питоне",
              "author": "Андрей Пронин",
              "price": 1200}] * 3
    context = {"books": books}
    return render(request, "index.html", context)
