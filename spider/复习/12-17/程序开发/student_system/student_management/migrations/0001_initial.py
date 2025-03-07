# Generated by Django 3.1.7 on 2021-11-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.IntegerField(verbose_name='学生ID')),
                ('risk', models.CharField(max_length=20, verbose_name='是否途径风险区')),
                ('reaction', models.CharField(max_length=20, verbose_name='是否出现新冠肺炎症状')),
                ('temperature', models.IntegerField(verbose_name='体温')),
                ('c_time', models.DateTimeField(verbose_name='提交时间')),
            ],
            options={
                'db_table': 'health',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_code', models.IntegerField(verbose_name='学号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('address', models.TextField(verbose_name='家庭住址')),
                ('faculty', models.CharField(max_length=10, verbose_name='学院')),
                ('major', models.CharField(max_length=20, verbose_name='专业')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
