from django.urls import path
from owner import views
urlpatterns = [
    path('books/add',views.AddBook.as_view(),name='add_book')
]