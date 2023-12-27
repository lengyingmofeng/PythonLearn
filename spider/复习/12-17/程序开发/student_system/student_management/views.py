from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.contrib import messages
from django.db.models import Q

from datetime import datetime
from .models import Student, Health


@require_GET
def student_index(request):
    '''
    ### 1.2 请补全代码
    '''

    return


def student_create(request):
    if request.method == 'GET':
        return render(request, 'student_create.html')
    if request.method == 'POST':
        '''
        ### 1.3 请补全代码
        '''

        return


def student_update(request):
    if request.method == 'GET':
        student_code = request.GET.get('student_code')
        if not student_code:
            return redirect('health:student_index')
        student = Student.objects.filter(student_code=student_code).first()
        context = {'student': student}
        return render(request, 'student_update.html', context=context)
    if request.method == 'POST':
        '''
        ### 1.3 请补全代码
        '''


        return


@require_GET
def student_delete(request):
    '''
    ### 1.3 请补全代码
    '''
    id = request.GET.get("student_code")
    Student.objects.filter(student_code=id).delete()
    return redirect("health:student_index")


@require_GET
def health_index(request):

    return


@require_GET
def health_risk(request):
    '''
    ### 1.4 请补全代码
    '''
    date_first = datetime(2021, 12, 7)
    date_last = datetime(2021, 12, 20)
    healths = Health.objects.filter(Q(c_time__gte=date_first) & Q(c_time__lte=date_last),
                                    Q(risk="是") | Q(reaction="是") | Q(temperature__gte=370)).all().order_by('c_time')
    for health in healths:
        reason = ""
        if health.risk == "是":
            reason = "途径风险区"
        if health.reaction == "是":
            reason = "新冠肺炎症状"
        if health.temperature >= 370:
            reason = "体温异常"
        student = Student.objects.filter(id=health.student_id).first()
        health.student = student
        health.reason = reason
    return render(request, "health_risk.html", context={"risk_obj": healths})
