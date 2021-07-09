from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


def index(request):
    template_name = 'views/index.html'

    some_books = Book.objects.all()[:4]
    some_read_books = Book.objects.filter(read=True)[:4]
    some_unread_books = Book.objects.filter(read=False)[:4]
    some_books_wishlist = Book.objects.filter(owned=False)[:4]

    all_read_books = Book.objects.filter(read=True)
    all_not_read_books = Book.objects.filter(read=False)
    currently_reading_books = ToReadBook.objects.filter(currently_reading=True)
    wishlist_books = Book.objects.filter(owned=False)

    save_books_in_model(all_read_books, DoneToReadBook)
    save_books_in_model(all_not_read_books, ToReadBook)
    save_books_in_model(currently_reading_books, CurrentReadingBook)
    save_books_in_model(wishlist_books, Wishlist)

    context = {
        'some_books': some_books,
        'some_read_books': some_read_books,
        'some_unread_books': some_unread_books,
        'some_books_wishlist': some_books_wishlist,
    }

    return render(request, template_name, context)


def save_books_in_model(books, model):
    for book in books:

        if not model.objects.filter(title=book.title, author=book.author, type=book.type).exists():
            new_entry = model(title=book.title,
                              author=book.author,
                              type=book.type)
            new_entry.save()


class AuthorsLister(APIView):

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorsSerializer(authors, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_post(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = AuthorsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        authors = self.get_post(pk)
        serializer = AuthorsSerializer(authors, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_post(pk)
        author.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksDetail(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class HistoryBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="History")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ComputerScienceBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Computer Science")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComputerScienceBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PsychologyBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Psychology")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PsychologyBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SalesBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Sales")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MarketingBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Marketing")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarketingBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BiographyBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Biography")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BiographyBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FinancesBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Finances")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinancesBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BusinessBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Business")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class NegotiationBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Negotiation")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NegotiationBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FictionBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Fiction")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FictionBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AutobiographyBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Autobiography")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutobiographyBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PeotryBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Poetry")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoetryBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MeditationsBooksLister(APIView):

    def get(self, request, format=None):
        books = Book.objects.filter(type="Meditations")
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeditationsBookDetails(APIView):

    def get_post(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        books = self.get_post(pk)
        serializer = BooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DoneToReadBooksLister(APIView):

    def get(self, request, format=None):
        read_books = DoneToReadBook.objects.all()
        serializer = DoneToReadBookSerializer(read_books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoneToReadBookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneToReadBooksDetail(APIView):

    def get_post(self, pk):
        try:
            return DoneToReadBook.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = DoneToReadBookSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):

        read_books = self.get_post(pk)
        serializer = DoneToReadBookSerializer(read_books, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        read_book = self.get_post(pk)
        read_book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ToReadBooksLister(APIView):

    def get(self, request, format=None):
        books = ToReadBook.objects.all()
        serializer = ToReadBooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToReadBooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToReadBooksDetail(APIView):

    def get_post(self, pk):

        try:
            return ToReadBook.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):

        post = self.get_post(pk)
        serializer = ToReadBooksLister(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):

        books = self.get_post(pk)
        serializer = ToReadBooksSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class WishlistLister(APIView):

    def get(self, request, format=None):
        wishlist_books = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist_books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WishlistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WishlistDetail(APIView):

    def get_post(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = WishlistSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        wishlist = self.get_post(pk)
        serializer = WishlistSerializer(wishlist, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wishlist = self.get_post(pk)
        wishlist.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentReadingBooksLister(APIView):

    def get(self, request, format=None):
        currently_reading_books = CurrentReadingBook.objects.all()
        serializer = CurrentReadingBookSerializer(currently_reading_books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrentReadingBookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentReadingBooksDetail(APIView):

    def get_post(self, pk):
        try:
            return CurrentReadingBook.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = CurrentReadingBookSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currently_reading_books = self.get_post(pk)
        serializer = CurrentReadingBookSerializer(currently_reading_books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        currently_reading_books = self.get_post(pk)
        currently_reading_books.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
