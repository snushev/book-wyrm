from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Review, Genre
from .forms import ReviewForm

# Create your views here.

# Book views

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
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