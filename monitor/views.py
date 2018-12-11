# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from monitor import models
# Create your views here.


@login_required
def index(request):
    return HttpResponse("this is monitor")




