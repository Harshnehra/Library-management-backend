from django.urls import path
from .views import BookListCreateView

urlpatterns = [
    path('list/', BookListCreateView.as_view(), name='book-list-create'),
    path('list/<int:book_id>/', BookListCreateView.as_view(), name='book-list-create'),
]
