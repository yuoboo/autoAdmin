from django.conf.urls import url
from monitor import views

urlpatterns = [
    url(r'index/$', views.monitor, name='monitor'),
    url(r'tree/nodes/$', views.tree_nodes, name='tree_nodes'),

    url(r'ztree/$', views.ztree, name='ztree'),
    url(r'test/tree/$', views.test_tree, name='test_tree')
]
