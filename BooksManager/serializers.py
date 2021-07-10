from .models import *
from rest_framework import serializers


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class DoneToReadBookSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = DoneToReadBook
        fields = '__all__'


class ToReadBooksSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = ToReadBook
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'


class CurrentReadingBookSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = CurrentReadingBook
        fields = '__all__'


class BookTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookType
        fields = '__all__'

