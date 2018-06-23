from django.db import models


# Create your models here.
# 学生类模板
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    learn = models.CharField(max_length=20)


# 教师类模板
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    teach = models.CharField(max_length=20)
    student = models.ManyToManyField(Student, through="OneClass")


# 班级类模板
class OneClass(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
