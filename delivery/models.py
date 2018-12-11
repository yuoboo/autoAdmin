# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from appconf.models import Project
# Create your models here.

DEPOLY_POLICY = (
    ('', ''),
    ('Direct', 'Direct'),
)


# 认证信息
class AuthInfo(models.Model):
    dis_name = models.CharField(u'认证标识', max_length=50, unique=True, blank=False)
    username = models.CharField(u'用户名', max_length=50, blank=True)
    password = models.CharField(u'密码', max_length=50, blank=True)
    private_key = models.CharField(u'秘钥', max_length=100, blank=True)
    desc = models.TextField(u'备注信息', max_length=200, blank=True)

    def __unicode__(self):
        return self.dis_name


class Delivery(models.Model):
    job_name = models.OneToOneField(Project, verbose_name=u'项目名')
    desc = models.TextField(u'项目描述', max_length=200, blank=True)
    deploy_policy =models.CharField(u'部署策略', choices=DEPOLY_POLICY, max_length=100)
    version = models.CharField(u'版本号', max_length=100, blank=True)
    build_clean = models.BooleanField('清理架构', default=False)
    rsync_del = models.BooleanField('同步清理', default=True)
    shell = models.CharField('shell', max_length=200, blank=True)
    shell_position = models.BooleanField(u'本地shell', default=False)
    status = models.BooleanField(u'部署状态', default=False)
    deploy_num = models.IntegerField(u'部署次数', default=0)
    bar_data = models.IntegerField(default=0)

    auth = models.ForeignKey(AuthInfo,
                             verbose_name='认证信息',
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL,
                             )

    def __unicode__(self):
        return self.job_name
