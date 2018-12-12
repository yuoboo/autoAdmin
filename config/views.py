# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
# Create your views here.
import ConfigParser as cp
from demo.settings import BASE_DIR
import os

CONFIG_PATH = os.path.join(BASE_DIR, 'demo.conf')


@login_required
def config(request):
    _cfg = cp.ConfigParser()
    if request.method == 'POST':
        _dict = request.POST
        _cfg.add_section('config')
        ansible_path = _cfg.set("config", "ansible_path", _dict["ansible_path"])
        roles_path = _cfg.set("config", "roles_path", _dict["roles_path"])
        playbook_path = _cfg.set("config", "playbook_path", _dict["playbook_path"])
        code_path = _cfg.set("config", "code_path", _dict["code_path"])
        scripts_path = _cfg.set("config", "scripts_path", _dict["scripts_path"])
        
        _cfg.add_section('mysql')
        mysql_user = _cfg.set("mysql", "mysql_user", _dict["mysql_user"])
        mysql_passwd = _cfg.set("mysql", "mysql_passwd", _dict["mysql_passwd"])
        mysql_host = _cfg.set("mysql", "mysql_host", _dict["mysql_host"])
        mysql_port = _cfg.set("mysql", "mysql_port", _dict["mysql_port"])
        mysql_db = _cfg.set("mysql", "mysql_db", _dict["mysql_db"])
        
        _cfg.add_section('redis')
        redis_host = _cfg.set("redis", "redis_host", _dict["redis_host"])
        redis_passwd = _cfg.set("redis", "redis_passwd", _dict["redis_passwd"])
        redis_port = _cfg.set("redis", "redis_port", _dict["redis_port"])
        redis_db = _cfg.set("redis", "redis_db", _dict["redis_db"])
        
        _cfg.add_section('log')
        log_path = _cfg.set("log", "log_path", _dict["log_path"])
        log_level = _cfg.set("log", "log_level", _dict["log_level"])
        
        with open(CONFIG_PATH, 'wb') as f:
            _cfg.write(f)
            
        return redirect('config')

    else:

        with open(CONFIG_PATH, 'r') as f:
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

        return render(request, 'config/config_list.html', locals())


def get_config(*args):
    _cfg = cp.ConfigParser()
    with open(CONFIG_PATH, 'r') as f:
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

    if len(args) > 1:
        _l = [vars()[i] for i in args]
        return tuple(_l)
    else:
        return vars()[args[0]]


