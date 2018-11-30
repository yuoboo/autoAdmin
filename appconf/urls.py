from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'appowner/$', views.owner, name='appowner'),
    url(r'appowner/add/$', views.owner_add, name='appowner_add'),
    url(r'appowner/edit/(?P<ids>\d+)/$', views.owner_edit, name='appowner_edit'),
    url(r'appowner/del/(?P<ids>\d+)/$', views.owner_del, name='appowner_del'),

    url(r'product/$', views.product, name='product'),
    url(r'product/add/$', views.product_add, name='product_add'),
    url(r'product/edit/(?P<ids>\d+)/$', views.product_edit, name='product_edit'),
    url(r'product/del/(?P<ids>\d+)/$', views.product_del, name='product_del'),

    url(r'project/$', views.project, name='project'),
    url(r'project/add/$', views.project_add, name='project_add'),
    url(r'project/edit/(?P<ids>\d+)/$', views.project_edit, name='project_edit'),
    url(r'project/del/(?P<ids>\d+)/$', views.project_del, name='project_del'),
]
