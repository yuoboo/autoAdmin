# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from delivery.models import Delivery
from delivery.forms import DeliveryForm, AuthInfoForm
from appconf.models import Project
from delivery.tasks import deploy
import os
# Create your views here.


@login_required
def delivery_list(request):
    deliverys = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', locals())


@login_required
def delivery_add(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u"新增成功"})
        return render(request, 'response_con.html', {"msg": form.errors})
    else:
        form = DeliveryForm()
        return render(request, 'delivery/delivery_add.html', locals())


@login_required
def delivery_edit(request, ids):
    obj = Delivery.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {"msg": u'新增成功'})
        return render(request, 'response_con.html', {"msg": form.errors})
    else:
        form = DeliveryForm(instance=obj)
        return render(request, 'delivery/delivery_edit.html', locals())


@login_required
def delivery_del(request, ids):
    obj = Delivery.objects.filter(id=ids)
    if obj:
        obj.first().delete()
        return render(request, 'response_con.html', {"msg": u'删除成功'})
    else:
        return render(request, 'response_con.html', {"msg": u'删除项不存在'})


@login_required
def delivery_deploy(request, ids):
    deli_obj = Delivery.objects.filter(id=ids).first()
    deli_obj.bar_data = 10
    deli_obj.deploy_num += 1
    deli_obj.status = True
    deli_obj.save()

    project_name = deli_obj.job_name.name
    os.system("mkdir -p /var/opt/demo/workspace/{}/code".format(project_name))
    os.system("mkdir -p /var/opt/demo/workspace/{}/logs".format(project_name))
    os.system("mkdir -p /var/opt/demo/workspace/{}/scripts".format(project_name))

    app_path = deli_obj.job_name.appPath
    if app_path == '/':
        return HttpResponse(u"项目部署路径不能为根目录")

    deploy.delay(ids)
    deli_obj.bar_data = 15
    return JsonResponse({"msg": u'部署任务已经提交'})


@login_required
def delivery_log2(request, ids):
    deli = Delivery.objects.filter(id=ids).first()
    return render(request, 'delivery/delivery_log.html', locals())


@login_required
def delivery_log(request, ids):
    data = ''
    try:
        pro = Delivery.objects.filter(id=ids).first()
        log_path = '/var/opt/demo/workspace/{0}/logs/deploy_{1}.log'.format(pro.job_name.name, pro.deploy_num)
        with open(log_path, 'rb') as f:
            con = f.readlines()
        for i in con:
            data += i.strip() + '<br>'
    except:
        data = "Nothing"
    return render(request, 'delivery/delivery_log.html', locals())
