from django.shortcuts import render
from CatoApp.models import *


def index(request):
    return render(request, 'index.html')


def login(request):
    # This if statement should not return true
    # AKA A user who has logged in should not be able to login again without logging out
    if request.session['login'] == 'in':
        request.session.flush()
    return render(request, 'login.html')


def verify_login(email,password):
    return User.objects.filter(email=email,password=password).count() == 1