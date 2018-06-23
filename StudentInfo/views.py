from django.shortcuts import render


# from django.http import request
# Create your views here.
def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def delete(request):
    return render(request, 'delete.html')


def query(request):
    return render(request, 'query.html')


def update(request):
    return render(request, 'update.html')
