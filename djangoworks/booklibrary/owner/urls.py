from django.urls import path
from owner import views
urlpatterns = [
    path('books/add',views.AddBook.as_view(),name='add_book'),
    path('books/all', views.BookList.as_view(), name='list_book'),
    path('books/<int:id>',views.BookDetailView.as_view(),name='bookbetail'),
    path('books/change/<int:id>', views.BookEditView.as_view(), name='book_edit'),
    path('books/delete/<int:id>', views.BookDeleteView.as_view(), name='book_delete')

]