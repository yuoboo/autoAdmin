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
