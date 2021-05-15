from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index1(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)
