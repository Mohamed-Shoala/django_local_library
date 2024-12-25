from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define root path for catalog
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('author/', views.AuthorListView.as_view(), name='author_list'),  # URL for listing authors
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),  # URL for author details

]
