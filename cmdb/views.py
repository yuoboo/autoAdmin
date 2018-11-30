# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Host, Idc
from .forms import HostForm, IdcForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def asset(request):
    hosts = Host.objects.all()

    return render(request, 'cmdb/asset.html', locals())


@login_required
def asset_add(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'保存成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = HostForm()
        return render(request, 'cmdb/asset_add.html', locals())


@login_required
def asset_edit(request, ids):
    host = Host.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'编辑成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = HostForm(instance=host)
        return render(request, 'cmdb/asset_edit.html', locals())


