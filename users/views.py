from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인 되었습니다.')
            return redirect('todos:home')
        else:
            messages.success(request, '로그인에 실패하였습니다.')
            return redirect('users:login')


def logout_user(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('users:home')
