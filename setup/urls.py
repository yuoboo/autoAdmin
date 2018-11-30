from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'job/$', views.job, name='job'),
    url(r'job/add$', views.job_add, name='job_add'),
]
