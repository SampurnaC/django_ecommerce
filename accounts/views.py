from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login(request):
    return render(request, 'accounts/login.html')

def logout_user(request):
    print('logged out')
    logout(request)

    return redirect('store:home')
