from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('accounts:login')
    else:
        form=UserRegisterForm()    
    context={'form': form}
    return render(request, 'accounts/register.html', context)

def logout_user(request):
    print('logged out')
    logout(request)
    messages.success(request, ('Logged out successfully'))
    return redirect('store:home')
