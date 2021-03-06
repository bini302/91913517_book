# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm, ReadForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    page = request.GET.get('page', '1')
    book_list = Book.objects.order_by('-create_date')
    paginator = Paginator(book_list, 3)
    page_obj = paginator.get_page(page)
    context = {'book_list': page_obj}
    return render(request, "polls1/book_list.html", context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'polls1/book_detail.html', context)


@login_required(login_url='common:login')
def read_create(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReadForm(request.POST)
        if form.is_valid():
            read = form.save(commit=False)
            read.author = request.user
            read.create_date = timezone.now()
            read.book = book
            read.save()
            return redirect('polls1:detail', book_id=book.id)
    else:
        form = ReadForm()
    context = {'book': book, 'form': form}
    return render(request, 'polls1/book_detail.html', context)


@login_required(login_url='common:login')
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.create_date = timezone.now()
            book.save()
            return redirect('polls1:index')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'polls1/book_form.html', context)


@login_required(login_url='common:login')
def book_modify(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('polls1:detail', book_id=book.id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.modify_date = timezone.now()
            book.save()
            return redirect('polls1:detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'polls1/book_form.html', context)
