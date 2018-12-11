from django.conf.urls import url
from config import views

urlpatterns = [
    url(r'list/$', views.config, name='config'),
]