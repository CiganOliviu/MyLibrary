from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('rest/authors/', views.AuthorsLister.as_view(), name='AuthorsList'),
    path('rest/authors/<int:pk>', views.AuthorDetail.as_view(), name='AuthorDetail'),

    path('rest/books/history/', views.HistoryBooksLister.as_view(), name='HistoryBooksLister'),
    path('rest/books/history/<int:pk>', views.HistoryBookDetails.as_view(), name='HistoryBookDetails'),

    path('rest/books/computer-science/', views.ComputerScienceBooksLister.as_view(), name='ComputerScienceBooksLister'),
    path('rest/books/computer-science/<int:pk>', views.ComputerScienceBookDetails.as_view(), name='ComputerScienceBookDetails'),

    path('rest/books/psychology/', views.PsychologyBooksLister.as_view(), name='PsychologyBooksLister'),
    path('rest/books/psychology/<int:pk>', views.PsychologyBookDetails.as_view(), name='PsychologyBookDetails'),

    path('rest/books/sales/', views.SalesBooksLister.as_view(), name='SalesBooksLister'),
    path('rest/books/sales/<int:pk>', views.SalesBookDetails.as_view(), name='SalesBookDetails'),

    path('rest/books/marketing/', views.MarketingBooksLister.as_view(), name='MarketingBooksLister'),
    path('rest/books/marketing/<int:pk>', views.MarketingBookDetails.as_view(), name='MarketingBookDetails'),

    path('rest/books/biography/', views.BiographyBooksLister.as_view(), name='BiographyBooksLister'),
    path('rest/books/biography/<int:pk>', views.BiographyBookDetails.as_view(), name='BiographyBookDetails'),

    path('rest/books/finances/', views.FinancesBooksLister.as_view(), name='FinancesBooksLister'),
    path('rest/books/finances/<int:pk>', views.FinancesBookDetails.as_view(), name='FinancesBookDetails'),

    path('rest/books/business/', views.BusinessBooksLister.as_view(), name='BusinessBooksLister'),
    path('rest/books/business/<int:pk>', views.BusinessBookDetails.as_view(), name='BusinessBookDetails'),

    path('rest/books/negotiation/', views.NegotiationBooksLister.as_view(), name='NegotiationBooksLister'),
    path('rest/books/negotiation/<int:pk>', views.NegotiationBookDetails.as_view(), name='NegotiationBookDetails'),

    path('rest/books/fiction/', views.FictionBooksLister.as_view(), name='FictionBooksLister'),
    path('rest/books/fiction/<int:pk>', views.FictionBookDetails.as_view(), name='FictionBookDetails'),

    path('rest/books/autobiography/', views.AutobiographyBooksLister.as_view(), name='AutobiographyBooksLister'),
    path('rest/books/autobiography/<int:pk>', views.AutobiographyBookDetails.as_view(), name='AutobiographyBookDetails'),

    path('rest/books/poetry/', views.PeotryBooksLister.as_view(), name='PeotryBooksLister'),
    path('rest/books/poetry/<int:pk>', views.PoetryBookDetails.as_view(), name='PoetryBookDetails'),

    path('rest/books/meditations/', views.MeditationsBooksLister.as_view(), name='MeditationsBooksLister'),
    path('rest/books/meditations/<int:pk>', views.MeditationsBookDetails.as_view(), name='MeditationsBookDetails'),

    path('rest/books/', views.BooksLister.as_view(), name='BooksList'),
    path('rest/books/<int:pk>', views.BooksDetail.as_view(), name='BooksDetail'),
    path('rest/read-books/', views.DoneToReadBooksLister.as_view(), name='ReadBookLister'),
    path('rest/read-books/<int:pk>', views.DoneToReadBooksDetail.as_view(), name='ReadBooksDetail'),
    path('rest/to-read-books/', views.ToReadBooksLister.as_view(), name='ToReadBookLister'),
    path('rest/read-books/<int:pk>', views.ToReadBooksDetail.as_view(), name='ToReadBooksDetail'),
    path('rest/wishlist/', views.WishlistLister.as_view(), name="WishlistLister"),
    path('rest/wishlist/<int:pk>', views.WishlistDetail.as_view(), name="WishlistDetail"),
    path('rest/current-reading-books/', views.CurrentReadingBooksLister.as_view(), name='CurrentReadingBooksLister'),
    path('rest/currently-reading-books/<int:pk>', views.CurrentReadingBooksDetail.as_view(), name='CurrentReadingBooksDetail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)