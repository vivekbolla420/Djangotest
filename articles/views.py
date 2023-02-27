from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.


def home(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/home.html', {'articles': articles})


def hi(request):
    return HttpResponse("hi")
