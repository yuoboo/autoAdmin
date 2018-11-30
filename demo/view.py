#encoding=utf8
from django.shortcuts import render,redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')
