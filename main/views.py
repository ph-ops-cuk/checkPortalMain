from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *


def home(request):
    # full list of checks
    checklist = Check.objects.all()
    total_checks = checklist.count()

    # full list of results
    resultlist = Result.objects.all()
    # retrieve filtered results
    totalfails = Result.objects.filter(status='Failed')
    totalfailscount = totalfails.count()

    totalpass = Result.objects.filter(status='Passed')
    totalpasscount = totalpass.count()

    test = Check.objects.filter(result__status='').count

    context = {'total_checks': total_checks, 'checklist': checklist, 'resultlist': resultlist, 'totalfails': totalfails,
               'totalfailscount': totalfailscount, 'totalpasscount': totalpasscount, 'test': test}

    return render(request, 'main/dashboard.html', context)


def checks(request):
    return render(request, 'main/checks.html')


def report(request):
    return HttpResponse('Report')
