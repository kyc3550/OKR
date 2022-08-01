from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User
# Create your views here.

def register(request):
    form = RegisterForm()
    context = {'forms' : form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                user_name = form.user_name,
                user_id = form.user_id,
                user_pw= form.user_pw,
                user_phone_number = form.user_phone_number,
                user_gender = form.user_gender,
            )
            user.save()
            return redirect('/')
        else:
            context['forms']  = form
        return render(request, 'user/register.html',context)
    elif request.method == 'GET':
        return render(request, 'user/register.html', context)

def login(request):
    form = LoginForm()
    context = {'forms':form}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['login_session'] = form.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else:
            context['forms']  = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
        return render(request, 'user/login.html',context)
    elif request.method == 'GET':
        return render(request, 'user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')