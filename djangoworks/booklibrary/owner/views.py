from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import BookForm
from .models import Books

# Create your views here.


class AddBook(View):
    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {'form': form}
        return render(request, 'addbook.html', context)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            book_name = form.cleaned_data.get('book_name')
            author = form.cleaned_data.get('author')
            price = form.cleaned_data.get('price')
            copies = form.cleaned_data.get('copies')
            qs = Books(book_name=book_name,author=author,price=price,copies=copies)
            qs.save()
            return render(request, 'addbook.html')
