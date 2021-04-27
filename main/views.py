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
    remaining = Check.objects.exclude(result__status='Passed').exclude(result__status='Failed').order_by('site_id')

    remaining_list = remaining
    paginator = Paginator(remaining_list, 7)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    checks_remain_count = total_checks - (Check.objects.filter(result__status='Passed').count() + Check.objects.filter(
        result__status='Failed').count())
    category = Category.objects.all()
    context = {'total_checks': total_checks, 'checklist': checklist, 'resultlist': resultlist, 'totalpass': totalpass,
               'totalfails': totalfails,
               'totalfailscount': totalfailscount, 'totalpasscount': totalpasscount, 'category': category,
               'remaining': remaining, 'checks_remain_count': checks_remain_count, 'page': page,
               'next_page_url': next_url, 'prev_page_url': prev_url}

    return render(request, 'main/dashboard.html', context)


def beta(request):
    return render(request, 'main/beta.html')


def report_percentage_stats(total, passed):
    percentage = (total / passed) * 100
    return percentage


def report(request):
    category_list = Category.objects.all
    total = Category.objects.count()
    passed = 5
    report_stats = report_percentage_stats(total, passed)
    # context = {'category': category, 'report_stats': int(report_stats)}
    context = {'category_list': category_list}
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


def result_create(request):
    form = ResultForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ResultForm(request.POST)
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
