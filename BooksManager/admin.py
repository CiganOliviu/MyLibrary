from django.contrib import admin
from .models import *


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'interesting_level')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'owned', 'read')

    def author(self, obj):
        return obj.author.first_name


class DoneToReadBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'mark')


class ToReadBooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'currently_reading')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'wanting_level')


class CurrentReadingBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type')


admin.site.register(Author, AuthorsAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookType, BookTypeAdmin)
admin.site.register(DoneToReadBook, DoneToReadBookAdmin)
admin.site.register(ToReadBook, ToReadBooksAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(CurrentReadingBook, CurrentReadingBookAdmin)

admin.site.site_header = "my-library"
