from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout

from myuser.models import MyUser
from myuser.forms import LoginForm, SignupForm
from django.conf import settings


def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get("password"))
            if user:
                login(request, user)
                # return render(request, 'index.html', {"form": form})
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, 'base.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname")
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'base.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
