# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
# Create your views here.


@login_required
def config(requset):
    return JsonResponse({"msg": 'config is ok'})