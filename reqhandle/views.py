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

def recommend(request):
    result = Book.objects.filter(id__lt=11)

    tmp = []

    for i in range(0, len(result)-1):
        tmp.append(model_to_dict(result[i]))

    data = dict()

    data['books'] = tmp

    #print json.dumps(data, ensure_ascii=False)

    return HttpResponse(json.dumps(data, ensure_ascii=False))


def search(request):

    bookname = request.POST['bookname']

    print bookname
    #return HttpResponse("data")
    #bookname = bookname.decode('utf8')

    result = Book.objects.filter(title__contains=bookname)

    tmp = []

    print len(result)

    for i in range(0, len(result)):
        tmp.append(model_to_dict(result[i]))

    data = dict()

    data['books'] = tmp

   # print json.dumps(data, ensure_ascii=False)

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


def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )
    return millis


def getcomment(request):

    arg = request.POST['isbn']
    print arg
    b = Book.objects.get(isbn=arg)

    result = b.comment_set.all()

    tmp = []
    obj = dict()

    for i in range(0, len(result)-1):
        obj['title'] = result[i].title
        obj['content'] = result[i].content
        obj['userid'] = result[i].user.userid
        obj['com_time'] = str(result[i].com_time)
        tmp.append(obj)

    data = dict()

    data['comment'] = tmp

    return HttpResponse(json.dumps(data, ensure_ascii=False))