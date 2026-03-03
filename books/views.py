from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Book, Review
from .forms import BookForm, ReviewForm, SearchForm 

# Create your views here.

# Book views

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_text = self.request.GET.get("query")

        if search_text:
            return queryset.filter(title__icontains=search_text) | queryset.filter(author__icontains=search_text)
        
        return queryset
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_has_reviewed'] = Review.objects.filter(
                book=self.get_object(),
                user=self.request.user
            ).exists()
        return context
    
class BookCreateView(LoginRequiredMixin, CreateView):
    form_class = BookForm
    model = Book
    template_name = 'books/book_add.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.pk
        return reverse('book-detail', kwargs={'pk': pk})

# Review views

class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    model = Review
    template_name = 'books/create_review.html'

    def form_valid(self, form):
        book_id = self.kwargs['pk']
        book_obj = Book.objects.get(pk=book_id)

        form.instance.book = book_obj
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.book.pk
        return reverse('book-detail', kwargs={'pk': pk})
    
class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    fields = ["review", "rating"]
    template_name = "books/create_review.html"
    
    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.book.pk})
    
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user
    
class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "books/delete_review.html"

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.book.pk})
    
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user