# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
# Create your views here.
import ConfigParser as cp
from demo.settings import BASE_DIR

CONFIG_FILE_NAME = '/demo.conf'


@login_required
def config(requset):
    _cfg = cp.ConfigParser()
    with open(BASE_DIR+CONFIG_FILE_NAME, 'r') as f:
        _cfg.readfp(f)

        ansible_path = _cfg.get('config', 'ansible_path')
        roles_path = _cfg.get("config", "roles_path")
        playbook_path = _cfg.get("config", "playbook_path")
        code_path = _cfg.get("config", "code_path")
        scripts_path = _cfg.get("config", "scripts_path")

        # mysql
        mysql_user = _cfg.get("mysql", "mysql_user")
        mysql_passwd = _cfg.get("mysql", "mysql_passwd")
        mysql_host = _cfg.get("mysql", "mysql_host")
        mysql_port = _cfg.get("mysql", "mysql_port")
        mysql_db = _cfg.get("mysql", "mysql_db")

        # redis
        redis_host = _cfg.get("redis", "redis_host")
        redis_passwd = _cfg.get("redis", "redis_passwd")
        redis_port = _cfg.get("redis", "redis_port")
        redis_db = _cfg.get("redis", "redis_db")

        # log
        log_path = _cfg.get("log", "log_path")
        log_level = _cfg.get("log", "log_level")

    return render(requset, 'config/config_list.html', locals())


@login_required
def config_edit(request):
    return JsonResponse({"msg": "edit"})


