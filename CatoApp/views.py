from django.shortcuts import render
from CatoApp.forms import *
from CatoApp.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.template import RequestContext


def search(request):
    if request.method == 'GET':
        return render(
            request,
            'search.html',
            {
                'search_form': SearchForm(),
                'search_result': SearchForm().matched_jobs()
            }
        )
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            return render(
                request,
                'search.html',
                {
                    'search_form': search_form,
                    'search_result': search_form.matched_jobs()
                }
            )
        else:
            return render(
                request,
                'search.html',
                {
                    'search_form': search_form,
                    'search_result': {}
                }
            )


def login(request):
    # This if statement should not return true
    # AKA A user who has logged in should not be able to login again without logging out
    if 'user_id' in request.session:
        return HttpResponseRedirect('/')

    # POST method process form
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            request.session['user_id'] = login_form.login()
            return HttpResponseRedirect('/profile/')
        return render(
            request,
            'login.html',
            {'login_form': login_form}
        )

    # other method (GET) display form
    return render(request, 'login.html', {'login_form': LoginForm()})


def logout(request):
    request.session.flush()  # delete everything; should I leave something alive?
    return HttpResponseRedirect('/')


def sign_up(request):
    # This if statement should not return true
    # AKA A user who has logged in should not be able to sign up
    if 'user_id' in request.session:
        logout(request)

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            request.session['user_id'] = sign_up_form.sign_up()
            return HttpResponseRedirect('/profile/')
        return render(
            request,
            'sign_up.html',
            {'sign_up_form': sign_up_form},
            RequestContext(request)
        )

    # other method (GET) display form
    return render(request, 'sign_up.html', {'sign_up_form': SignUpForm()})


def profile(request):
    if 'user_id' not in request.session:
        return render(request, 'login.html', {'login_form': LoginForm()})
    return render(
        request,
        'profile.html',
        {
            'user': User.objects.get(id=request.session['user_id']),
            'skills': Skill.objects.filter(id__in=UserHasSkill.objects.filter(user_id=request.session['user_id']))
        }
    )


def json_all_skills(request):
    return HttpResponse(serializers.serialize("json", Skill.objects.all()), content_type='application/json')
