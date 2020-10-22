from django.db import models
from datetime import date

from accounts.models import Account


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    '''
    author added as foreign key, if author is deleted, field here in book would be set to NULL
    By default, 
        genre is added as many to many field relation, a single book can have more than 1 genres
        there will be only one copy of a book available
        date_added set to today for new instance
        ratings shall be displayed upto 2 decimal places
        short description will be of 100 character length
    '''
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    copies = models.IntegerField(default=1)
    date_added = models.DateField(default=date.today())
    ratings = models.DecimalField(decimal_places=2)
    short_desc = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    cover_picture = models.ImageField(upload_to='book_photos/')

    def __str__(self):
        return self.title

    def display_genre(self):
        '''
        In case there are more than one genre per book, all the available genres for a book are
        joined with comma and space. 
        '''
        return ', '.join(item for item in genre)
