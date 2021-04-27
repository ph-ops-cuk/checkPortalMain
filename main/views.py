from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import CheckForm, ResultForm


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

    # test = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').count
    # remaining_count = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').count
    remaining = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').order_by('site_id')
    checks_remain = total_checks - (Check.objects.filter(result__status='Passed').count() + Check.objects.filter(result__status='Failed').count())
    category = Category.objects.all()
    context = {'total_checks': total_checks, 'checklist': checklist, 'resultlist': resultlist, 'totalpass': totalpass, 'totalfails': totalfails,
               'totalfailscount': totalfailscount, 'totalpasscount': totalpasscount, 'category': category,
               'remaining': remaining, 'checks_remain': checks_remain}

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


def check_create(request):
    form = CheckForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = CheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def check_update(request, pk):
    check = Check.objects.get(id=pk)
    form = CheckForm(instance=check)

    if request.method == 'POST':
        form = CheckForm(request.POST, instance=check)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def result_update(request, pk):
    result = Result.objects.get(id=pk)
    check = Check.objects.get(id=pk)
    form = ResultForm(instance=result)

    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def CheckList(request):
    object_list = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').order_by('site_id')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})
