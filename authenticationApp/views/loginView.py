import sys

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from authenticationApp.forms import LoginForm


def loginView(request):
    form = LoginForm()
    context = {
        'form':  form
    }

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect(reverse("authenticationApp:home"))

    return render(request, 'authenticationApp/login.html', context)


sys.modules[__name__] = loginView
