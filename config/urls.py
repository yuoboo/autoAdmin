from django.conf.urls import url
from config import views

urlpatterns = [
    url(r'list/$', views.config, name='config'),
    url(r'edit/$', views.config_edit, name='config_edit'),

]
