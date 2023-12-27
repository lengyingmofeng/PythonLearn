from django.db import models

# Create your models here.


class Health(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(verbose_name='学生ID')
    risk = models.CharField(max_length=20, verbose_name='是否途径风险区')
    reaction = models.CharField(max_length=20, verbose_name='是否出现新冠肺炎症状')
    temperature = models.IntegerField(verbose_name='体温')
    c_time = models.DateTimeField(verbose_name='提交时间')

    class Meta:
        db_table = 'health'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_code = models.IntegerField(verbose_name='学号')
    name = models.CharField(max_length=10, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    address = models.TextField(verbose_name='家庭住址')
    faculty = models.CharField(max_length=10, verbose_name='学院')
    major = models.CharField(max_length=20, verbose_name='专业')

    class Meta:
        db_table = 'student'    