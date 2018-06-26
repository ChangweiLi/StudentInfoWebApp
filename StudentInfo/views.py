from django.http import HttpResponse
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
        Student.objects.create(name=name, age=age, learn=learn)  # 在student 表里新建一条记录
        # return render(request, 'add.html',)
    return render(request, 'add.html')


def delete(request):
    name = request.GET.get('name')
    type1 = request.GET.get('type1')
    # type 为 1 表示执行数据库查询操作
    # if type1 == '1':
    #     # 查询所在记录
    #     try:
    #         stu: Student = Student.objects.filter(name=name).get()
    #     except Exception:
    #         return HttpResponse("无此记录")
    #     return render(request, 'delete.html', {'stu': stu})
    # type 为 2 表示执行数据库确认删除操作
    if type1 == '2':
        try:
            Student.objects.filter(name=name).get()
        except Exception:
            return HttpResponse("无此记录")
        Student.objects.filter(name=name).delete()
        return render(request, 'delete.html', {'msg': '删除成功'})
    return render(request, 'delete.html')


def update(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    learn = request.GET.get('learn')
    type1 = request.GET.get('type1')
    # type 为1表示执行数据库操作，否则只是跳转页面
    if type1 == '1':
        stu = Student.objects.get(name=name)
        stu.name = name
        stu.age = age
        stu.learn = learn
        stu.save()
        return render(request, "update.html", {'msg': '修改成功'})
    return render(request, 'update.html')


def query(request):
    name = request.GET.get('name')
    type1 = request.GET.get('type1')
    # type 为1表示执行数据库操作，否则只是跳转页面
    if type1 == '1':
        if name == 'all':
            stu_list = Student.objects.all()
            return render(request, 'query.html', {'stu_list': stu_list})
        try:
            Student.objects.filter(name=name).get()
        except Exception:
            return HttpResponse("无此记录")
        stu = Student.objects.get(name=name)  # 在student 表里查询一条记录
        return render(request, 'query.html', {'stu': stu})

    return render(request, 'query.html')
