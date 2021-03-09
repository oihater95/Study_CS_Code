from django.shortcuts import render
from django.http.response import HttpResponse

def index(resquest):
    return HttpResponse('This is articles/index')

def mail(request):
    return HttpResponse('MYmail: oihater95@gmail.com')
