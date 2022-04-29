from django.shortcuts import render,redirect
from .forms import registerForm, loginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Successful Registered!")
            return redirect('home')
    else:
        form = registerForm()
    context = {
        'form':form
    }
    return render(request, 'userauth/auth.html', context)


def login_request(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                   return redirect(request.POST.get('next'))
                return redirect('home')
        
        else:
            messages.error(request, "Username or Password is Incorrect")
            redirect('login')
    else:
        form = loginForm()
    context = {
        'form':form
    }
    return render(request, 'userauth/login.html', context)