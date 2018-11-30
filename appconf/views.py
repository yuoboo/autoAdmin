# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product, Project, AppOwner
from .forms import ProductForm, ProjectForm, AppOwnerForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# 项目
@login_required
def project(request):
    projects = Project.objects.all()
    return render(request, 'appconf/project.html', locals())


@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'新建项目成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = ProjectForm()
        return render(request, 'appconf/project_add.html', locals())


@login_required
def project_edit(request, ids):
    proj = Project.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'编辑项目成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = ProjectForm(instance=proj)
        return render(request, 'appconf/project_edit.html', locals())


@login_required
def project_del(request, ids):
    proj = Project.objects.filter(id=ids)
    if proj:
        proj.first().delete()
        return render(request, 'response_con.html', {'msg': u'删除项目成功'})
    return render(request, 'response_con.html', {'msg': u'删除项目失败'})


# 产品线
@login_required
def product(request):
    products = Product.objects.all()
    return render(request, 'appconf/product.html', locals())


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'新建产品线成功'})
        return render(request, 'response_con.html', {'msg': form.errors})

    else:
        form = ProductForm()
        return render(request, 'appconf/product_add.html', locals())


@login_required
def product_edit(request, ids):
    pro = Product.objects.filter(id=ids)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': '编辑完成'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = ProductForm(instance=pro)
        return render(request, 'appconf/product_edit.html', locals())


@login_required
def product_del(request, ids):
    pro = Product.objects.filter(id=ids)
    if pro:
        pro.first().delete()
        return render(request, 'response_con.html', {'msg': u'删除产品线成功'})
    return render(request, 'response_con.html', {'msg': u'删除产品线失败'})


# 负责人
@login_required
def owner(request):
    owners = AppOwner.objects.all()
    return render(request, 'appconf/appowner.html', locals())


@login_required
def owner_add(request):
    if request.method == 'POST':
        form = AppOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'创建负责人成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = AppOwnerForm()
        return render(request, 'appconf/appowner_add.html', locals())


@login_required
def owner_edit(request, ids):
    owner = AppOwner.objects.filter(id=ids).first()
    if request.method == 'POST':
        form = AppOwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'修改成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = AppOwnerForm(instance=owner)
        return render(request, 'appconf/appowner_edit.html', locals())


@login_required
def owner_del(request, ids):
    owner = AppOwner.objects.filter(id=ids)
    if owner:
        owner.first().delete()
        return render(request, 'response_con.html', {'msg': u'删除成功'})
    return render(request, 'response_con.html', {'msg': u'删除项不存在'})

