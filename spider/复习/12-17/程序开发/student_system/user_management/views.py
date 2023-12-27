from django.contrib import messages, auth
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

# 1.1 3分


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        '''
        ### 1.1 请补全代码
        '''
    return


def logout(request):
    if request.method == "GET":
        request.session['user'] = None
        return redirect('user:login')
