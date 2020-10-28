from django.contrib import admin
from books.models import Book, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ratings', 'date_added')


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
