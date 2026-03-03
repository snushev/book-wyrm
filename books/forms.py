from django import forms
from .models import Review, Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year_published', 'description', 'genre', 'cover']

class SearchForm(forms.Form):
    query = forms.CharField(label='', required=False, max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Search for a book...'}))