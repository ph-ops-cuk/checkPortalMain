from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'main/dashboard.html')


def status(request):
    return HttpResponse('Status')


def report(request):
    return HttpResponse('Report')
