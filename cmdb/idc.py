# encoding=utf8
from .models import Idc
from .forms import IdcForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required
def idc(request):
    '''
    机房列表信息
    :param request:
    :return:
    '''
    idcs = Idc.objects.all()
    return render(request, 'cmdb/idc.html', locals())


@login_required
def idc_add(request):
    if request.method == 'POST':
        form = IdcForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'新增机房成功'})
        return render(request, 'response_con.html', {'msg': form.errors})

    else:
        form = IdcForm()
        return render(request, 'cmdb/idc_add.html', locals())


@login_required
def idc_edit(request, ids):
    '''
    机房信息编辑
    :param request:
    :param ids: 机房编号
    :return: 机房对象form
    '''
    idc = Idc.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = IdcForm(request.POST, instance=idc)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'保存成功'})
        return render(request, 'response_con.html', {'msg': form.errors})

    else:
        form = IdcForm(instance=idc)
        return render(request, 'cmdb/idc_edit.html', locals())


@login_required
def idc_del(request, ids):
    idc = Idc.objects.filter(id=ids)
    if idc:
        idc.first().delete()
        return HttpResponse(u'删除成功')
    return HttpResponse(u'删除项不存在')