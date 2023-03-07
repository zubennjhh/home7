from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BooksView.as_view(), name='books'),
    path('books/<int:id>/', views.BooksFullView.as_view(), name='details'),
    path('books/<int:id>/change/', views.BooksUpdateView.as_view(), name='update'),
    path('books/<int:id>/delete/', views.BooksDeleteView.as_view(), name='delete'),
    path('add-books/', views.BooksCreateView.as_view(), name='create'),
    path('add-comment/', views.CreateCommentView.as_view(), name='comment'),
]