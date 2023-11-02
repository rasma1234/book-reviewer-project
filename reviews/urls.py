
from django.urls import path
from .views import BookListView, BookDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("reviews/", ReviewListView.as_view(), name="review_list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
]



