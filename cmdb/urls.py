from django.conf.urls import url
from . import views, idc


urlpatterns = [
    url(r'asset/$', views.asset, name='asset'),
    url(r'asset/add/$', views.asset_add, name='asset_add'),
    url(r'asset/edit/(?P<ids>\d+)/$', views.asset_edit, name='asset_edit'),

    url(r'idc/$', idc.idc, name='idc'),
    url(r'idc/add/$', idc.idc_add, name='idc_add'),
    url(r'idc/edit/(?P<ids>\d+)/$', idc.idc_edit, name='idc_edit'),
    url(r'idc/del/(?P<ids>\d+)/$', idc.idc_del, name='idc_del'),

]
