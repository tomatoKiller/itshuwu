from digg.models import Comment

__author__ = 'wu'

from django.shortcuts import render
from django.http import HttpResponse
from digg.models import Book

def search(request):
    bookname = request.POST['bookname']

    result = Book.objects.filter(title__contains=bookname)

    ss = ""

    for tmp in result:
        ss += tmp.title + '<br/>'
    return HttpResponse(ss)
    #return render(result, 'home/search.html', result)

def comment(request):
    arg = request.POST['isbn']
    result = Book.objects.get(isbn=arg)

    c = Comment()




def index(request):
    return render(request, 'home/index.html')