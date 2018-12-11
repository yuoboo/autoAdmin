from django.conf.urls import url
from delivery import views


urlpatterns = [
    url(r'list/$', views.delivery_list, name='delivery'),
    url(r'add/$', views.delivery_add, name='delivery_add'),
    url(r'edit/(?P<ids>\d+)/$', views.delivery_edit, name='delivery_edit'),
    url(r'del/(?P<ids>\d+)/$', views.delivery_del, name='delivery_del'),

    url(r'log/(?P<ids>\d+)$', views.delivery_log, name='delivery_log'),

    url(r'delpoy/(?P<ids>\d+)/$', views.delivery_deploy, name='delivery_deploy'),

]
