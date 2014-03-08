from django.shortcuts import render
from django.http import HttpResponse
from digg.digfunc import Analyse_Url
import string

def digg(request):

    #for i in range(1, 10):

    result1 = Analyse_Url('0')
    result1.start()

    result1.join()

    return HttpResponse("OK")
'''
    result2 = Analyse_Url('20')
    result2.start()

    result3 = Analyse_Url('40')
    result3.start()

    result4 = Analyse_Url('60')
    result4.start()

    result5 = Analyse_Url('80')
    result5.start()

    result6 = Analyse_Url('100')
    result6.start()




    result1.join()
    result2.join()
    result3.join()
    result4.join()
    result5.join()
    result6.join()
'''



'''
    result = Analyse_Url(chr(2))
    result.start()

    result = Analyse_Url(chr(3))
    result.start()
'''