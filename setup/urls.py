from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'job/$', views.job, name='job'),
    url(r'job/add$', views.job_add, name='job_add'),
    url(r'job/edit/(?P<ids>\d+)/$', views.job_edit, name='job_edit'),
    url(r'job/del/(?P<ids>\d+)/$', views.job_del, name='job_del'),

    url(r'interval/$', views.interval, name='interval'),
    url(r'interval/add/$', views.interval_add, name='interval_add'),
    url(r'interval/edit/(?P<ids>\d+)/$', views.interval_edit, name='interval_edit'),

    url(r'crontab/$', views.crontab, name='crontab'),
    url(r'crontab/add/$', views.crontab_add, name='crontab_add'),
    url(r'crontab/edit/(?P<ids>\d+)/$', views.crontab_edit, name='crontab_edit'),

    url(r'job_result/$', views.job_result, name='job_result'),
    url(r'job_result/del/(?P<ids>\d+)/$', views.job_result_del, name='job_result_del'),

]
