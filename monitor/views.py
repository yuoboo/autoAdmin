# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from cmdb.models import Host
import json
from monitor import models
# Create your views here.


@login_required
def monitor(request):
    hosts = Host.objects.all()
    return render(request, 'monitor/monitor_index.html', locals())


@csrf_exempt
@login_required
def tree_nodes(request):
    print 'tree_nodes'
    host_node = get_host_nodes()
    return JsonResponse(host_node, safe=False)


def get_host_nodes():
    '''
    获取服务器节点数据: {"name": "服务器节点", "open": "true", "children": [{"name": hostname, "url": "", "target": ""}]}
    :return:
    '''
    hosts = Host.objects.all()
    data = []
    for h in hosts:
        _d = dict()
        _d["name"] = h.hostname
        _d["url"] = "http://www.baidu.com"
        _d["target"] = "myframe"
        data.append(_d)
    result = {"name": "服务器节点", "open": "true", "children": data}
    return json.dumps(result)


@login_required
def ztree(request):
    return render(request, 'monitor/ztreeDemo.html', locals())


@csrf_exempt
def test_tree(request):
    _dict = request.POST
    _dict2 = request.GET
    print _dict, _dict2
    _id = _dict.get("id", "") if _dict.get("id", "") else ''
    _name = _dict.get("name", "") if _dict.get("name", "") else ''
    print _id
    print _name
    if _id:
        _d = get_data(_id, _name)
        return JsonResponse(json.dumps(_d), safe=False)
    else:
        _d = [
            {"id": "1", "name": 't01', "open": True,
             "children": [{"id": "1.1", "name": 't01-01'},
                          {"id": "1.2", "name": 't01-02', 'url': 'http://www.baidu.com', 'target': 'myframe'}]
             },

            {"id": "2", "name": 't02', "open": False,
             "children": [{"id": "2.1", "name": 't02-01', "isParent": True},
                          {"id": "2.2", "name": 't02-02'}]
             },
        ]
        # _d = get_data('1', 't1')
        return JsonResponse(json.dumps(_d), safe=False)


def get_data(_id, _name):
    data = []
    for i in xrange(1, 4):
        d = dict()
        d['id'] = _id+'.'+str(i)
        d["name"] = "{0}-{1}".format(_name, i)
        d["isParent"] = True if i < 3 and len(_id.split('.')) < 4 else False
        data.append(d)
    return data
