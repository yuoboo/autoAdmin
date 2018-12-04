# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PeriodicTaskForm, IntervalForm, CrontabForm, PeriodicTask, IntervalSchedule, CrontabSchedule

# Create your views here.


@login_required
def job(request):
    jobs = PeriodicTask.objects.all()
    return render(request, 'setup/job.html', locals())


@login_required
def job_add(request):
    if request.method == 'POST':
        form = PeriodicTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'任务创建成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = PeriodicTaskForm()
        return render(request, 'setup/job_add.html', locals())


@login_required
def job_edit(request, ids):
    obj = PeriodicTask.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = PeriodicTaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u'修改任务成功'})
        return render(request, 'response_con.html', form.errors)
    else:
        form = PeriodicTaskForm(instance=obj)
        return render(request, 'setup/job_edit.html', locals())


@login_required
def interval(request):
    intervals = IntervalSchedule.objects.all()
    return render(request, 'setup/interval.html', locals())


@login_required
def interval_add(request):
    if request.method == 'POST':
        form = IntervalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u'新增时间间隔成功'})
        return render(request, 'response_con.html', form.errors)
    else:
        form = IntervalForm()

        return render(request, 'setup/interval_add.html', locals())


@login_required
def interval_edit(request, ids):
    obj = IntervalSchedule.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = IntervalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u'修改时间间隔成功'})
        return render(request, 'response_con.html', form.errors)
    else:
        form = IntervalForm(instance=obj)
        return render(request, 'setup/interval_add.html', locals())


@login_required
def crontab(request):
    crontabs = CrontabSchedule.objects.all()

    return render(request, 'setup/crontab.html', locals())


@login_required
def crontab_add(request):
    if request.method == 'POST':
        form = CrontabForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u"新增定时时间成功"})
        return render(request, 'response_con.html', form.errors)
    else:
        form = CrontabForm()
        return render(request, 'setup/crontab_add.html', locals())


@login_required
def crontab_edit(request, ids):
    obj = CrontabSchedule.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = CrontabForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u"定时任务编辑成功"})
        return render(request, 'response_con.html', form.errors)
    else:
        form = CrontabForm(instance=obj)
        return render(request, 'setup/crontab_add.html', locals())