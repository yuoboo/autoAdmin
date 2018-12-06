# encoding=utf8
from demo.celery import app
from celery import shared_task
from appconf.models import Host
import sh
from subprocess import Popen, PIPE

SCRIPTS_DIR = "/var/opt/adminset/data/scripts/"


@shared_task
def command(host, name):
    h = Host.objects.filter(hostname=host).first()
    cmd = sh.ssh("root@"+h.ip, name)
    return str(cmd).strip()


@shared_task
def script(host, name):
    h = Host.objects.filter(hostname=host).first()
    sh.scp(SCRIPTS_DIR+name, "root@{0} /tem/{1}".format(h.ip, name))
    cmd = "ssh root@"+h.ip + "sh /tem/{0}".format(name)
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    data = p.communicate()
    return data

