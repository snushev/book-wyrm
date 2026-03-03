from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('add/', views.BookCreateView.as_view(), name='book-add'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/review/', views.ReviewCreateView.as_view(), name='add-review'),
    path('review/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='update-review'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='delete-review'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)