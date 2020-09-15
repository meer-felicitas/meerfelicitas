from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contact.html')

def resources(request):
    return render(request,'resources.html')

def articles(request):
    return render(request,'articles.html')