from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    cover = models.ImageField(upload_to='covers', null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        unique_together = ('book', 'user')

    RATING_CHOICES = {
        1: 1,     
        2: 2,     
        3: 3,     
        4: 4,     
        5: 5,     
    }

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title + " by " + self.user.username

    