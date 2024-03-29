from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def u_register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('table')
    context = {'form': form}
    return render(request, 'registration/u_register.html', context)
