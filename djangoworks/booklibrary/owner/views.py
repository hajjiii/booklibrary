from django.shortcuts import render, redirect
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
        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # book_name = form.cleaned_data.get('book_name')
            # author = form.cleaned_data.get('author')
            # price = form.cleaned_data.get('price')
            # copies = form.cleaned_data.get('copies')
            # qs = Books(book_name=book_name,author=author,price=price,copies=copies)
            # qs.save()
            form.save()
            return render(request, 'addbook.html')
        else:
            context = {'form':form}
            return render(request,'addbook.html', context)

class BookList(View):
    def get(self,request,*args,**kwargs):
        qs = Books.objects.all()
        print(qs)
        context = {
            'books': qs
        }
        return render(request,'listbook.html',context)

class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id = kwargs.get('id')
        qs = Books.objects.get(id=id)
        context = {'book':qs}
        return render(request,'bookdetail.html',context)

class BookEditView(View):
    def get(self,request,*args,**kwargs):
        id= kwargs.get('id')
        qs = Books.objects.get(id=id)
        form = BookForm(instance=qs)
        context ={'form': form}
        return render(request,'bookedit.html',context)
    def post(self,request,*args,**kwargs):
        id = kwargs.get('id')
        qs = Books.objects.get(id=id)
        form = BookForm(request.POST,files=request.FILES,instance=qs)
        if form.is_valid():
            form.save()
            return render(request,'bookedit.html')
        else:
            context={'form':form}
            return render(request,'bookedit.html',context)

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        qs = Books.objects.get(id=id)
        qs.delete()
        books = Books.objects.all()
        context ={
            'book':qs,
            'books':books

        }
        return render(request,'listbook.html',context)
