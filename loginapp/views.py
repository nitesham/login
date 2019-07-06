from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

@login_required
def index(request):
    return render(request,"home.html")


def Registration(request):
    if request.method == 'POST':
        print("come inside")
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("true")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,"registration/registration.html", {'form': form})