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

    test = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').count
    remaining = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed')
    category = Category.objects.all()
    context = {'total_checks': total_checks, 'checklist': checklist, 'resultlist': resultlist, 'totalfails': totalfails,
               'totalfailscount': totalfailscount, 'totalpasscount': totalpasscount, 'test': test, 'category': category,
               'remaining': remaining}

    return render(request, 'main/dashboard.html', context)


def beta(request):
    return render(request, 'main/beta.html')


def report(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'main/report.html', context)


def tasks(request):
    return render(request, 'main/tasks.html')


def calendar(request):
    return render(request, 'main/calendar.html')
