from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hi dears")

def test_fun(request):
    return render(request,'test.html')