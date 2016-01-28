# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
    test1 = Test(name='Django.cc')
    test1.save()
    return HttpResponse("<h3>Insert Completed</h3>")
