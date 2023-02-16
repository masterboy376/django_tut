# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('home')

def rempun(request):
    # get the text
    rawText=request.GET.get('text','')
    return HttpResponse('rempun')

def capfirst(request):
    return HttpResponse('capfirst')

def remspace(request):
    return HttpResponse('remspace')

def remnewline(request):
    return HttpResponse('remnewline')

def charcount(request):
    return HttpResponse('charcount')