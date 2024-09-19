from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('book/<int:pk>', book, name="book"),
    path('book_add', addBook, name="book_add"),
    path('book_update/<int:pk>', updateBook, name="book_update"),
    path('book_delete/<int:pk>', deleteBook, name="book_delete"),
    path('review_add/<int:pk>', addReview, name="review_add"),
    path('review/<int:pk>', review_detail, name="review_detail"),
    path('review_edit/<int:pk>', review_edit, name='review_edit'),
    path('review_delete/<int:pk>', review_delete, name='review_delete'),
    path('login', loginPage, name="login"),
    path('logout', logoutUser, name="logout"),
    path('register', registerUser, name="register"),
]