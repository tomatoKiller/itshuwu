import json
from django.utils.timezone import now
from digg.models import Comment
from rege.models import Customer
from django.forms.models import model_to_dict

from django.shortcuts import render
from django.http import HttpResponse
from digg.models import Book


def index(request):
    return render(request, 'reqhandle/index.html')


def search(request):



    bookname = request.POST['bookname']

    print bookname
    #return HttpResponse("data")


    result = Book.objects.filter(title__contains=bookname)

    tmp = []

    for i in range(0, len(result)-1):
        tmp.append(model_to_dict(result[i]))

    data = dict()

    data['books'] = tmp

    print json.dumps(data, ensure_ascii=False)

    return HttpResponse(json.dumps(data, ensure_ascii=False))




'''
    ss = ""

    for tmp in result:
        ss += tmp.title + '<br/>'
    return HttpResponse(ss)
    #return render(result, 'home/search.html', result)
'''


def comment(request):
    arg = request.POST['comment']
    arg = json.loads(arg)

    b = Book.objects.get(isbn=arg['isbn'])
    u = Customer.objects.get(userid=arg['userid'])
    c = Comment(content=arg['comment'], com_time=now(), title=arg['title'], book=b, user=u)
    c.save()

    b.score = arg['score']
    b.save()

    return HttpResponse("OK")


def getcomment(request):

    arg = request.POST['isbn']

    b = Book.objects.get(isbn=arg)

    result = b.comment_set.all()

    tmp = []

    for i in range(0, len(result)-1):
        tmp.append(model_to_dict(result[i]))

    data = dict()

    data['comment'] = tmp

    return HttpResponse(json.dumps(data, ensure_ascii=False))