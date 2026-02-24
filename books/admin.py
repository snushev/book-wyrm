from django.contrib import admin
from .models import Genre, Book, Review

# Register your models here.

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Review)