from django.shortcuts import render
from StudentInfo.models import Student, OneClass


# from django.http import request
# Create your views here.
def index(request):
    return render(request, 'index.html')


def add(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    learn = request.GET.get('learn')
    type1 = request.GET.get('type1')
    # type 为1表示执行数据库操作，否则只是跳转页面
    if type1 == '1':
        Student.objects.create(name=name)  # 在student 表里新建一条记录
    return render(request, 'add.html')


def delete(request):
    name = request.GET.get('name')
    # age = request.GET.get('age')
    # learn = request.GET.get('learn')
    type1 = request.GET.get('type1')
    # type 为1表示执行数据库操作，否则只是跳转页面
    if type1 == '1':
        # 在student 表里新建一条记录
        Student.objects.filter(name=name).delete()
    return render(request, 'delete.html', {'stu': "删除成功"})

    # rname =
    return render(request, 'delete.html')


def query(request):
    name = request.GET.get('name')
    type1 = request.GET.get('type1')
    # type 为1表示执行数据库操作，否则只是跳转页面
    if type1 == '1':
        stu = Student.objects.get(name=name)  # 在student 表里新建一条记录
        return render(request, 'query.html', {'stu': stu})

    return render(request, 'query.html')


def update(request):
    return render(request, 'update.html')
