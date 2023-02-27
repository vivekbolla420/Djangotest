from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def home(request):
    return HttpResponse("this is home page")
