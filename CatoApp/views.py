from django.shortcuts import render
from django.shortcuts import render_to_response
from CatoApp.forms import *
from CatoApp.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext


def index(request):
    return render(request, 'index.html')


def login(request):
    # This if statement should not return true
    # AKA A user who has logged in should not be able to login again without logging out
    if request.session.has_key('user_id'):
        logout(request)

    # POST method process form
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            request.session['user_id'] = login_form.login()
            return HttpResponseRedirect('/')
        return render(
            request,
            'login.html',
            {'login_form': login_form},
            RequestContext(request)
        )

    # other method (GET) display form
    return render(
        request,
        'login.html',
        {'login_form': LoginForm()},
        RequestContext(request)
    )


def logout(request):
    request.session.flush() # delete everything; should I leave something alive?


def sign_up(request):
    # This if statement should not return true
    # AKA A user who has logged in should not be able to sign up
    if request.session.has_key('user_id'):
        logout(request)

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            request.session['user_id'] = sign_up_form.sign_up()
            return HttpResponseRedirect('/')
        return render(
            request,
            'sign_up.html',
            {'sign_up_form': sign_up_form},
            RequestContext(request)
        )

    # other method (GET) display form
    return render(
        request,
        'sign_up.html',
        {'sign_up_form': SignUpForm()},
        RequestContext(request)
    )

