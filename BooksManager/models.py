from django.db import models
from .data_source import BOOKS_TYPES, POSSIBLE_MARKS
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    birthday = models.DateTimeField(auto_now_add=True)
    year = models.DateField()
    description = models.TextField(default="")

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author', default=1)
    read = models.BooleanField(default=False)
    type = models.CharField(max_length=25, choices=BOOKS_TYPES, default=0)
    owned = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='books/',
                              default='/books/default.jpg')

    def __str__(self):
        return self.title


class DoneToReadBook(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=25, choices=BOOKS_TYPES, default=0)
    mark = models.CharField(max_length=2, choices=POSSIBLE_MARKS, default=0)

    def __str__(self):
        return self.title


class ToReadBook(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=25, choices=BOOKS_TYPES, default=0)
    currently_reading = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    title = models.CharField(max_length=150, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=25, choices=BOOKS_TYPES, default=0)
    wanting_level = models.CharField(max_length=2, choices=POSSIBLE_MARKS, default=0)

    def __str__(self):
        return self.title


class CurrentReadingBook(models.Model):
    title = models.CharField(max_length=150, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=25, choices=BOOKS_TYPES, default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
