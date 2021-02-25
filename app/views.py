from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book, Opinion


def books(request):
    MAX = 20
    if request.GET.get("pk"):
        given_pk = request.GET.get("pk")
        book = get_object_or_404(Book, pk=given_pk)
        opinions = Opinion.objects.filter(book=book)
        data = {
            "results": {
                "pk": book.pk,
                "author": book.author,
                "title": book.title,
                "type": book.type,
                "isbn": book.isbn,
                "opinions": list(
                    opinions.values("pk", "book", "rate", "description", "isbn")
                ),
            }
        }
    elif request.GET.get("title"):
        given_title = request.GET.get("title")
        books = Book.objects.filter(title__contains=given_title)
        data = {"results": list(books.values("pk", "author", "title", "type", "isbn"))}
    else:
        books = Book.objects.all()[:MAX]
        data = {"results": list(books.values("pk", "author", "title", "type", "isbn"))}
    return JsonResponse(data)
