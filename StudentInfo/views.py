from django.shortcuts import render
from StudentInfo.models import Student,OneClass


# from django.http import request
# Create your views here.
def index(request):
    return render(request, 'index.html')


def add(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    learn = request.GET.get('learn')
    # Student.objects.get_or_create(name=name, age=age, learn=learn)
    # print(name)
    # print(age)
    return render(request, 'add.html')


def delete(request):

    return render(request, 'delete.html')


def query(request):

    return render(request, 'query.html')


def update(request):

    return render(request, 'update.html')
