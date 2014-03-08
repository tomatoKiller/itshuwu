from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse
from django.utils.timezone import now
from django.contrib.auth import authenticate, login, logout
from rege.models import Customer
import json


def log_in(request):
    arg = request.POST['login']

    f=open('aa.txt', 'w')
    f.write(arg)
    f.close()

    arg = json.loads(arg)



    c = Customer.objects.filter(userid=arg['name'])
    if not c:
        return HttpResponse("2")
    elif c[0].passwd != arg['password']:
        return HttpResponse("1")
    else:
        return HttpResponse("0")



def log_out(request):
    logout(request)
    return HttpResponse("OK")


def register(request):

    #return HttpResponse("OK")
    arg = request.POST['register']

    f=open('aa.txt', 'w')
    f.write(arg)
    f.close()

    arg = json.loads(arg)

    print arg['name']
    print arg['password']
    if Customer.objects.filter(userid=arg['name']):
        return HttpResponse("1")

    u = Customer(userid=arg['name'], email="fjsdjff@163.com", passwd=arg['password'], reg_time=now())
    u.save()

    return HttpResponse("0")