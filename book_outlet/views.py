from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book
# Create your views here.

def index(request):
    all_books = Book.objects.all().order_by("-rating")
    number_of_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "total_number_of_books": number_of_books,
        "average_rating": avg_rating
    })

def book_detail(request, slug):
    """try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()""" 
    book = get_object_or_404(Book, slug=slug) #same effect, just a oneliner
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating ,
        "is_bestselling": book.is_bestselling
    })