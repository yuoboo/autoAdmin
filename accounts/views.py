# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from .models import UserInfo
from django.http import HttpResponse, HttpResponseRedirect
from forms import LoginUserForm, AddUserForm, EditUserForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return HttpResponse('this is index')


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET' and request.GET.has_key('next'):
        next_page = request.GET.get('next')
        if next_page == '/accounts/logout/':
            next_page = '/'
    else:
        next_page = '/'

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        auth_user = auth.authenticate(username=username, password=password)
        form = LoginUserForm(request.POST)

        if form.is_valid():
            if auth_user is not None:
                if auth_user.is_active:
                    auth.login(request, auth_user)
                    print request.POST['next']
                    return redirect(request.POST['next'])
                else:
                    return render(request, 'response_con.html', {'msg': u'请先激活用户'})
        return render(request, 'response_con.html', {'msg': form.errors})

    else:
        form = LoginUserForm()
        context = {
            'form': form,
            'next': next_page,
        }
        return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))


@login_required
def user_add(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            form.save()
            return render(request, 'response_con.html', {'msg': u'创建成功'})
        return render(request, 'response_con.html', {'msg': form.errors})

    elif request.method == "GET":
        form = AddUserForm()
        return render(request, 'accounts/user_add.html', locals())


@login_required
def user_list(request):

    users = UserInfo.objects.filter(is_del=False).all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/user_list.html', context)


@login_required
def user_edit(request, ids):
    user = auth.get_user_model().objects.filter(id=ids).first()

    # print user.has_perm('accounts.add_userinfo')

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'response_con.html', {'msg': u'保存成功'})
        return render(request, 'response_con.html', {'msg': form.errors})
    else:
        form = EditUserForm(instance=user)
        return render(request, 'accounts/user_edit.html', locals())


@login_required
def password_change(request):
    pass