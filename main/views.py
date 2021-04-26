from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from .models import *

def home(request):
    checklist = Check.objects.all()
    resultlist = Result.objects.all()
    total_checks = checklist.count()

    totalfails = Result.objects.filter(status='Failed')
    totalfailscount = totalfails.count()
    totalpass = Result.objects.filter(status='Passed')
    totalpasscount = totalpass.count()

    context = {'total_checks': total_checks, 'checklist': checklist, 'resultlist': resultlist, 'totalfails': totalfails, 'totalfailscount': totalfailscount, 'totalpasscount': totalpasscount}

    return render(request, 'main/dashboard.html', context)


def checks(request):
    return render(request, 'main/checks.html')


def report(request):
    return HttpResponse('Report')
