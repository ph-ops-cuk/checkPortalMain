from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from datetime import date



# Create your views here.
from .models import Check, Category, Result
from .forms import CheckForm, ResultForm


def home(request):
    # full list of checks
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
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
               'next_page_url': next_url, 'prev_page_url': prev_url, 'd1': d1}

    return render(request, 'main/dashboard.html', context)


def betapage(request):
    return render(request, 'main/beta.html')


def report_percentage_stats(total, passed):
    percentage = (total / passed) * 100
    return percentage


def reportpage(request):
    total_results_complete = Category.objects.all()
    total_check_categorys = Check.objects.all()
    total_results_failed = Result.objects.filter(status='Failed')
    total_categories = Category.objects.count()
    total_results_passed = 73

    complete_list = {}
    for item in total_check_categorys:
        if item.category_id.name in complete_list:
            complete_list[item.category_id.name] += 1
        else:
            complete_list[item.category_id.name] = 1

    failed_list = {}
    for item in total_results_failed:
        if item.check_id.category_id.name in failed_list:
            failed_list[item.check_id.category_id.name] += 1
        else:
            failed_list[item.check_id.category_id.name] = 1

    def mergeDict(failed_list, complete_list):
        ''' Merge dictionaries and keep values of common keys in list'''
        new_list = {**failed_list, **complete_list}
        for key, value in new_list.items():
            if key in failed_list and key in complete_list:
                new_list[key] = [value, failed_list[key]]
            else:
                new_list[key] = [value, 0]
        return new_list

    # complete_list = {
    #     "Backup": 3,
    #     "DataDomain": 5,
    #     "AntiVirus": 2,
    #     "Storage": 9,
    #     "Snapshots": 9,
    #     "RecoverPoint": 9,
    #     "VMware": 3
    # }
    # failed_list = {
    #     "Backups": 1,
    #     "DataDomains": 3,
    #     "VMware": 2,
    #     "Storage": 2
    # }

    new_list = mergeDict(failed_list, complete_list)

    report_stats = report_percentage_stats(total_categories, total_results_passed)
    # context = {'category': category, 'report_stats': int(report_stats)}
    context = {'total_results_passed': total_results_passed, 'total_results_failed': total_results_failed,
               'failed_list': failed_list, 'new_list': new_list,
               'complete_list': complete_list, 'total_check_categorys': total_check_categorys}
    return render(request, 'main/report.html', context)


def taskpage(request):
    return render(request, 'main/tasks.html')


def calendar(request):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    context = {'d1': d1
               }
    return render(request, 'main/calendar.html')


def create_check(request):
    form = CheckForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = CheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def create_result(request):
    form = ResultForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def update_check(request, pk):
    check = Check.objects.get(id=pk)
    form = CheckForm(instance=check)

    if request.method == 'POST':
        form = CheckForm(request.POST, instance=check)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/check_form.html', context)


def update_result(request, pk):
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


def checkpage(request, pk):
    check = Check.objects.get(id=pk)

    context = {'check': check}
    return render(request, 'main/check.html', context)
