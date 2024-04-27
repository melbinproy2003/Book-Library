from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
from .forms import AuthorForm,BookForm
# Create your views here.

        # normal method

# def creatBook(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#         book = Book(title=title, price=price)
#         book.save()
#         return redirect('view')
#     return render(request,'book.html')

def listBook(request):
    name = request.session['username']
    book = Book.objects.all()
    paginator=Paginator(book,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'webadmin/home.html',{'books':book,'page':page,'name':name})

def details(request,book_id):
    name = request.session['username']
    book = Book.objects.get(id=book_id)
    return render(request,'webadmin/details.html',{'books':book,'name':name})

# def updateBook(request,book_id):
#     book = Book.objects.get(id=book_id)

#     if request.method == 'POST':
#         title= request.POST.get('title')
#         price= request.POST.get('price')
#         book.title=title
#         book.price=price
#         book.save()
#         return redirect('view')

#     return  render(request,'webadmin/update.html',{'book':book})

def deleteBook(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('view')

                # using  form  method

def creatBook(request):
    name = request.session['username']
    if request.method == 'POST' and request.FILES:
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form=BookForm()
    return render(request,'webadmin/book.html',{'form':form,'name':name})

def creatAuthor(request):
    name = request.session['username']
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request,'webadmin/author.html',{'form':form,'name':name})

def updateBook(request, book_id):
    name = request.session['username']
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = BookForm(instance=book)
    return render(request, 'webadmin/update.html', {'form': form,'name':name})


def SerachBox(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query)|Q(author__name__icontains=query))
    else:
        book=[]

    context={'books':books,'query':query}
    return render(request,'webadmin/search.html',context)
