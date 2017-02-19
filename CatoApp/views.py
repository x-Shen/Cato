from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Nothing to see here; it\'s still a test page</h1>')